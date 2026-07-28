import genanki
from utils.styles import build_css
import random
import os
import tempfile
from fastapi.responses import FileResponse
from fastapi import BackgroundTasks
from services.audio import AudioService
from services.image import ImageService

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

    async def prepare_audio(self, entries):
        audio_service = AudioService(
            lang=self.definition_options.source_language, media_folder=self.media_folder
        )
        audio = {}
        terms = [entry.term for entry in entries]
        audio_urls = {
            entry.term: entry.audio_url for entry in entries if entry.audio_url
        }
        if self.definition_source == "dictionary" and self.use_dictionary_audio:
            audio = await audio_service.fetch_many(terms, audio_urls)
        else:
            audio = audio_service.generate_many(terms)
        await audio_service.close_session()
        return audio

    async def prepare_images(self, entries):
        terms = [entry.term for entry in entries]
        image_service = ImageService(self.media_folder)
        images = await image_service.fetch_many(terms)
        await image_service.close_session()
        return images

    async def prepare_media(self, entries):
        audio = {}
        images = {}
        if self.definition_options.card_fields.audio:
            audio = await self.prepare_audio(entries)
        if self.definition_options.card_fields.image:
            images = await self.prepare_images(entries)
        return audio, images

    def create_note(self, entry, has_audio, has_image) -> genanki.Note:
        audio = f"[sound:{entry.term}.mp3]" if has_audio else ""
        image = f"<img src='{entry.term}.png'>" if has_image else ""
        return genanki.Note(
            model=self.model,
            fields=[
                entry.term,
                entry.part_of_speech or "",
                entry.definition,
                entry.example or "",
                ", ".join(entry.synonyms) if entry.synonyms else "",
                ", ".join(entry.antonyms) if entry.antonyms else "",
                audio,
                image,
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
        deck_name: str,
        background_tasks: BackgroundTasks,
    ):
        (audio, images) = await self.prepare_media(entries)
        media_files = list(audio.values()) + list(images.values())
        notes = [
            self.create_note(
                entry,
                entry.term in audio,
                entry.term in images,
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
