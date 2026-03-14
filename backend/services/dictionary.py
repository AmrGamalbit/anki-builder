# This is the deck generator for dictionaries.
# Simply provide data and a deck name to the constructor,
# and it will generate and store the deck. You can then call export_deck() to save it.
from services.base import BaseDeckGenerator


class DictionaryDeckGenerator(BaseDeckGenerator):
    def __init__(self):
        super().__init__()

    def build(self, data, deck_name: str = None):
        if deck_name != None:
            self.deck_name = deck_name
        notes = []
        for entry in data:
            for meaning in entry.meanings:
                for definition in meaning.definitions:
                    front = f"{entry.term}<br>({meaning.part_of_speech})"
                    back = f"{definition.text}"
                    example = definition.example if definition.example else ""
                    note = self.create_note(front, back, example)
                    notes.append(note)
        self.deck = self.create_deck(notes, self.deck_name)
