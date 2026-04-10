# This is the base generator that all other generators will inherit from.
import genanki
import random
import tempfile
from abc import ABC, abstractmethod

from services.pronunciation import PronunciationService
from services.pictogram import PictogramService
from utils.styles import build_css
from models.requests import StyleSettings
import os
from fastapi.responses import FileResponse
from fastapi import BackgroundTasks

MODEL_FIELDS = [
    {"name": "Term"},
    {"name": "Result"},
    {"name": "Pronunciation"},
    {"name": "Picture"},
]

MODEL_TEMPLATES = [
    {
        "name": "Card 1",
        "qfmt": "{{Term}}",
        "afmt": '<span class="highlight">{{FrontSide}}</span><hr id="answer">{{Result}}<br>{{Picture}}<br>{{Pronunciation}}',
    },
]


class BaseDeckGenerator(ABC):
    def __init__(
        self,
        style: StyleSettings,
        include_pronunciation: bool = False,
        include_pictogram: bool = False,
        target_language: str = "en",
        source_language: str = "en",
        mode: str = "definition",
    ):
        self.model = genanki.Model(
            model_id=1234567890,
            name="AnkiBuilderModel",
            fields=MODEL_FIELDS,
            templates=MODEL_TEMPLATES,
            css=build_css(style.model_dump()),
        )
        self.deck = None
        self.deck_name: str = "My Deck"
        self.temp_dir = tempfile.TemporaryDirectory()
        self.media_folder = self.temp_dir.name
        self.include_pictogram: bool = include_pictogram
        self.include_pronunciation: bool = include_pronunciation
        self.target_language = target_language
        self.source_language = source_language
        self.mode = mode

    def create_note(
        self,
        entry: tuple,
        has_pronunciation: bool,
        has_pictogram: bool,
    ) -> genanki.Note:
        term, front, back = entry
        lookup = term if self.mode == "definition" else back
        sound = f"[sound:{lookup}.mp3]" if has_pronunciation else ""
        image = f"<img src='{lookup}.png'>" if has_pictogram else ""
        return genanki.Note(model=self.model, fields=[front, back, sound, image])

    def create_deck(self, notes: list, deck_name: str) -> genanki.Deck:
        deck = genanki.Deck(deck_id=random.randrange(1 << 30, 1 << 31), name=deck_name)
        for note in notes:
            deck.add_note(note)
        return deck

    async def prepare_media(self, terms: list[str], pronunciation_urls=None):
        media_files = []
        available_pictograms = []
        available_pronunciations = []
        if self.include_pictogram:
            self.pictogram_service = PictogramService()
            pictograms = await self.pictogram_service.fetch_many(
                terms, self.media_folder
            )
            if pictograms:
                available_pictograms = pictograms.keys()
                media_files.extend(pictograms.values())
            await self.pictogram_service.close_session()

        if self.include_pronunciation:
            if self.mode == "definition":
                self.pronunciation_service = PronunciationService(
                    lang=self.source_language
                )
            else:
                self.pronunciation_service = PronunciationService(
                    lang=self.target_language
                )
            pronunciations = await self.get_pronunciations(terms, pronunciation_urls)
            if pronunciations:
                available_pronunciations = pronunciations.keys()
                media_files.extend(pronunciations.values())
            await self.pronunciation_service.close_session()

        return media_files, available_pictograms, available_pronunciations

    @abstractmethod
    async def get_pronunciations(self, terms: list[str]) -> str | None:
        pass

    def get_pictograms(self, terms: list[str]):
        self.pictogram.fetch_many(terms)

    @abstractmethod
    def parse_content(self):
        pass

    def get_lockup_term(self, entry):
        return entry.term if self.mode == "definition" else entry.result

    async def export_deck(self, data, deck_name, background_tasks: BackgroundTasks):
        notes = []
        entries, pronunciation_urls = self.parse_content(data)
        terms = [self.get_lockup_term(entry) for entry in data]
        (
            media_files,
            available_pictograms,
            available_pronunciations,
        ) = await self.prepare_media(terms, pronunciation_urls)
        for entry in entries:
            lookup_term = entry[0] if self.mode == "definition" else entry[-1]
            note = self.create_note(
                entry,
                lookup_term in available_pronunciations,
                lookup_term in available_pictograms,
            )
            notes.append(note)

        deck = self.create_deck(notes, deck_name)

        package = genanki.Package(deck)
        package.media_files = media_files
        deck_path = os.path.join(self.media_folder, f"{deck_name}.apkg")
        package.write_to_file(deck_path)
        background_tasks.add_task(self.temp_dir.cleanup)
        return FileResponse(
            path=deck_path,
            filename=f"{deck_name}.apkg",
            media_type="application/octet-stream",
        )
