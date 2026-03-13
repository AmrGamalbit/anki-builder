import genanki
import random

MODEL = genanki.Model(
    model_id=1234567890,
    name="AnkiBuilderModel",
    fields=[{"name": "Term"}, {"name": "Result"}, {"name": "Example"}],
    templates=[
        {
            "name": "Card 1",
            "qfmt": "{{Term}}",
            "afmt": '{{FrontSide}}<hr id="answer">{{Result}}<br><br>{{Example}}',
        },
    ],
)


# This is the base generator that all other generators will inherit from.
class BaseDeckGenerator:
    def __init__(self):
        self.deck = None
        self.deck_name: str = "My Deck"

    def create_note(self, term: str, result: str, example: str) -> genanki.Note:
        return genanki.Note(model=MODEL, fields=[term, result, example])

    def create_deck(self, notes: list, deck_name: str) -> genanki.Deck:
        deck = genanki.Deck(deck_id=random.randrange(1 << 30, 1 << 31), name=deck_name)
        for note in notes:
            deck.add_note(note)
        return deck

    def export_deck(self):
        package = genanki.Package(self.deck)
        package.write_to_file(f"{self.deck_name}.apkg")
        return "Deck was created! No worries"


# This is the deck generator for dictionaries.
# Simply provide data and a deck name to the constructor,
# and it will generate and store the deck. You can then call export_deck() to save it.
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


# This is the deck generator for dictionaries.
# Simply provide data and a deck name to the constructor,
# and it will generate and store the deck. You can then call export_deck() to save it.
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
                    front = f"{entry.term} - {meaning.part_of_speech}"
                    back = f"{definition.text}"
                    example = definition.example if definition.example else ""
                    note = self.create_note(front, back, example)
                    notes.append(note)
        self.deck = self.create_deck(notes, self.deck_name)
