# This is the base generator that all other generators will inherit from.
import genanki
import random
import tempfile
from abc import ABC, abstractmethod

from services.pronunciation import PronunciationService
from services.pictogram import PictogramService


css = """
.card {
  font-family: 'Segoe UI', sans-serif;
  font-size: 20px;
  color: #1a1a1a;
  background-color: #ffffff;
  text-align: center;
  padding: 20px;
  line-height: 1.6;
}

.card.night_mode {
  background-color: #1e1e1e;
  color: #e8e8e8;
}

hr {
  border: none;
  border-top: 1px solid #ddd;
  margin: 16px 0;
}

b, strong {
  color: #2563eb;
}

code {
  background: #f3f4f6;
  padding: 2px 6px;
  border-radius: 4px;
  font-family: monospace;
  font-size: 0.9em;
}

.night_mode code {
  background: #2d2d2d;
}
"""

model = genanki.Model(
    model_id=1234567890, name="My Model", fields=[...], templates=[...], css=css
)
MODEL = genanki.Model(
    model_id=1234567890,
    name="AnkiBuilderModel",
    fields=[
        {"name": "Term"},
        {"name": "Result"},
        {"name": "Pronunciation"},
        {"name": "Picture"},
    ],
    templates=[
        {
            "name": "Card 1",
            "qfmt": "{{Term}}",
            "afmt": '{{FrontSide}}<hr id="answer">{{Result}}<br>{{Picture}}<br>{{Pronunciation}}',
        },
    ],
    css=css,
)


class BaseDeckGenerator(ABC):
    def __init__(
        self,
        include_pronunciation: bool = False,
        include_pictures: bool = False,
        target_language: str = "en",
    ):
        self.deck = None
        self.deck_name: str = "My Deck"
        self.media_files: list[str] = []
        self.temp_dir = tempfile.TemporaryDirectory()
        self.pronunciation = (
            PronunciationService(target_language) if include_pronunciation else None
        )
        self.pictogram = PictogramService() if include_pictures else None

    def create_note(
        self,
        term: str,
        front: str,
        result: str,
    ) -> genanki.Note:

        if self.pronunciation:
            pronunciation_path = self.get_pronunciation_path(term)
            self.media_files.append(pronunciation_path)

        if self.pictogram:
            pictogram_path = self._get_pictogram(term)
            if pictogram_path:
                self.media_files.append(pictogram_path)

        return genanki.Note(
            model=MODEL,
            fields=[
                front,
                result,
                f"[sound:{term}.mp3]" if self.pronunciation else "",
                f"<img src='{term}.png'>" if self.pictogram and pictogram_path else "",
            ],
        )

    def create_deck(self, notes: list, deck_name: str) -> genanki.Deck:
        deck = genanki.Deck(deck_id=random.randrange(1 << 30, 1 << 31), name=deck_name)
        for note in notes:
            deck.add_note(note)
        return deck

    @abstractmethod
    def get_pronunciation_path(self, term: str) -> str | None:
        pass

    def _get_pictogram(self, term: str):
        pictogram_url = self.pictogram.get_url(term)
        pictogram_path = self.pictogram.fetch_pictogram(
            pictogram_url, self.temp_dir.name
        )
        return pictogram_path

    def export_deck(self):
        package = genanki.Package(self.deck)
        package.media_files = self.media_files
        package.write_to_file(f"{self.deck_name}.apkg")
        self.temp_dir.cleanup()
        return "Deck was created! No worries"
