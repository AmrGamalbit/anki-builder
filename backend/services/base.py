# This is the base generator that all other generators will inherit from.
import genanki
import random
import tempfile
import os
from gtts import gTTS
import requests

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
    fields=[{"name": "Term"}, {"name": "Result"}, {"name": "Pronunciation"}],
    templates=[
        {
            "name": "Card 1",
            "qfmt": "{{Term}}",
            "afmt": '{{FrontSide}}<hr id="answer">{{Result}}<br><br>{{Pronunciation}}',
        },
    ],
    css=css,
)


class BaseDeckGenerator:
    def __init__(self):
        self.deck = None
        self.deck_name: str = "My Deck"
        self.media_files: list[str] = []
        self.temp_dir = tempfile.TemporaryDirectory()
        self.include_pronunciation: bool = False
        self.lang: str = "en"

    def create_note(
        self,
        term: str,
        result: str,
        use_dictionary_audio: bool,
        pronunciation_url: str | None = None,
    ) -> genanki.Note:
        if self.include_pronunciation:
            if not use_dictionary_audio:
                audio_path = self._generate_pronunciation(term)
            else:
                if pronunciation_url is not None:
                    audio_path = self._fetch_pronunciation(term, pronunciation_url)
                else:
                    audio_path = self._generate_pronunciation(term)
            self.media_files.append(audio_path)
        return genanki.Note(
            model=MODEL,
            fields=[
                term,
                result,
                f"[sound:{term}.mp3]" if self.include_pronunciation else "",
            ],
        )

    def create_deck(self, notes: list, deck_name: str) -> genanki.Deck:
        deck = genanki.Deck(deck_id=random.randrange(1 << 30, 1 << 31), name=deck_name)
        for note in notes:
            deck.add_note(note)
        return deck

    def _generate_pronunciation(self, term: str) -> str:
        audio_path = os.path.join(self.temp_dir.name, f"{term}.mp3")
        gTTS(text=term.split("<")[0], lang=self.lang, slow=False).save(audio_path)
        return audio_path

    def _fetch_pronunciation(self, term: str, pronunciation_url: str) -> str:
        audio_path = os.path.join(self.temp_dir.name, f"{term}.mp3")
        response = requests.get(
            pronunciation_url, headers={"User-Agent": "Mozilla/5.0"}
        )
        response.raise_for_status()
        with open(audio_path, mode="wb") as file:
            file.write(response.content)
        return audio_path

    def export_deck(self):
        package = genanki.Package(self.deck)
        package.media_files = self.media_files
        package.write_to_file(f"{self.deck_name}.apkg")
        self.temp_dir.cleanup()
        return "Deck was created! No worries"
