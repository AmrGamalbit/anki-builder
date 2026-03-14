# This is the deck generator for AI models.
# Simply provide data and a deck name to the constructor,
# and it will generate and store the deck. You can then call export_deck() to save it.
from services.base import BaseDeckGenerator


class AIDeckGenerator(BaseDeckGenerator):
    def __init__(self):
        super().__init__()

    def build(self, data, deck_name: str = None):
        if deck_name != None:
            self.deck_name = deck_name
        notes = [
            self.create_note(entry.term, entry.result, entry.example) for entry in data
        ]
        self.deck = self.create_deck(notes, self.deck_name)
