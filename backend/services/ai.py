# This is the deck generator for AI models.
# Simply provide data and a deck name to the constructor,
# and it will generate and store the deck. You can then call export_deck() to save it.
from services.base import BaseDeckGenerator


class AIDeckGenerator(BaseDeckGenerator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_pronunciation_path(self, term: str):
        path = self.pronunciation.generate_pronunciation(term, self.temp_dir.name)
        return path

    def build(self, data, deck_name: str = None):
        if deck_name is not None:
            self.deck_name = deck_name
        notes = [
            self.create_note(
                entry.term, f"{entry.term}<br>{entry.example}", entry.result
            )
            for entry in data
        ]
        self.deck = self.create_deck(notes, self.deck_name)
