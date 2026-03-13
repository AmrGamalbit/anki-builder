# This is the base generator that all other generators will inherit from.
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
