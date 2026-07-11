import genanki
from utils.styles import build_css
import random
import os
import tempfile
from fastapi.responses import FileResponse
from fastapi import BackgroundTasks
from services.pronunciation import PronunciationService
from services.pictogram import PictogramService

MODEL_FIELDS = [
    {"name": "Term"},
    {"name": "PartOfSpeech"},
    {"name": "Definition"},
    {"name": "Example"},
    {"name": "Synonyms"},
    {"name": "Antonyms"},
    {"name": "Pronunciation"},
    {"name": "Picture"},
]

MODEL_TEMPLATES = [
    {
        "name": "Card 1",
        "qfmt": "{{Term}}<br><small>{{PartOfSpeech}}</small><br><em>{{Example}}</em>",
        "afmt": "<span class='highlight'>{{FrontSide}}</span><hr id='answer'>{{Definition}}<br>{{#Synonyms}}<small>🔄 {{Synonyms}}</small>{{/Synonyms}} {{#Antonyms}}<small>🔃 {{Antonyms}}</small>{{/Antonyms}}<br>{{Picture}}<br>{{Pronunciation}}",
    },
]


class DeckGenerator:
    def __init__(self, definition_options, appearance_options):
        self.definition_options = definition_options
        self.definition_source = self.definition_options.source
        self.use_dictionary_audio = getattr(
            self.definition_options, "use_dictionary_audio", False
        )
        self.model = genanki.Model(
            model_id=random.randrange(1 << 30, 1 << 31),
            name="AnkiBuilderModel",
            fields=MODEL_FIELDS,
            templates=MODEL_TEMPLATES,
            css=build_css(appearance_options.model_dump()),
        )
        self.temp_dir = tempfile.TemporaryDirectory()
        self.media_folder = self.temp_dir.name

    async def prepare_pronunciations(self, terms, pronunciations_url=[]):
        pronunciation_service = PronunciationService(
            lang=self.definition_options.source_language, media_folder=self.media_folder
        )
        if self.definition_source == "dictionary" and self.use_dictionary_audio:
            pronunciations = await pronunciation_service.fetch_many(
                terms, pronunciations_url
            )
        else:
            pronunciations = pronunciation_service.generate_many(terms)
        await pronunciation_service.close_session()
        if pronunciations:
            return list(pronunciations.keys()), list(pronunciations.values())
        return [], []

    async def prepare_pictograms(self, terms):
        pictogram_service = PictogramService(media_folder=self.media_folder)
        pictograms = await pictogram_service.fetch_many(terms)
        await pictogram_service.close_session()
        if pictograms:
            return list(pictograms.keys()), list(pictograms.values())
        return [], []

    async def prepare_media(self, terms, pronunciation_urls=[]):
        available_pronunciations, pronunciation_files = [], []
        available_pictograms, pictogram_files = [], []
        media_files = []
        if self.definition_options.include_pronunciation:
            (
                available_pronunciations,
                pronunciation_files,
            ) = await self.prepare_pronunciations(terms, pronunciation_urls)
        if self.definition_options.include_pictogram:
            available_pictograms, pictogram_files = await self.prepare_pictograms(terms)
        media_files = pronunciation_files + pictogram_files
        return media_files, available_pronunciations, available_pictograms

    def create_note(self, entry, has_pronunciation, has_pictogram) -> genanki.Note:
        sound = f"[sound:{entry.term}.mp3]" if has_pronunciation else ""
        picture = f"<img src='{entry.term}.png'>" if has_pictogram else ""
        return genanki.Note(
            model=self.model,
            fields=[
                entry.term,
                entry.part_of_speech or "",
                entry.definition,
                entry.example or "",
                ", ".join(entry.synonyms) if entry.synonyms else "",
                ", ".join(entry.antonyms) if entry.antonyms else "",
                sound,
                picture,
            ],
        )

    def create_deck(self, notes: list, deck_name: str) -> genanki.Deck:
        deck = genanki.Deck(deck_id=random.randrange(1 << 30, 1 << 31), name=deck_name)
        for note in notes:
            deck.add_note(note)
        return deck

    async def export_deck(
        self,
        entries,
        pronunciation_urls: list[str],
        deck_name: str,
        background_tasks: BackgroundTasks,
    ):
        audio_urls = [entry.audio_url for entry in entries]
        terms = [entry.term for entry in entries]
        (
            media_files,
            available_pronunciations,
            available_pictograms,
        ) = await self.prepare_media(terms, audio_urls)
        notes = [
            self.create_note(
                entry,
                entry.term in available_pronunciations,
                entry.term in available_pictograms,
            )
            for entry in entries
        ]
        deck = self.create_deck(notes, deck_name)
        package = genanki.Package(deck)
        package.media_files = media_files
        deck_path = os.path.join(tempfile.gettempdir(), f"{deck_name}.apkg")
        package.write_to_file(deck_path)
        background_tasks.add_task(self.temp_dir.cleanup)
        return FileResponse(
            path=deck_path,
            filename=f"{deck_name}.apkg",
            media_type="application/octet-stream",
        )
