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


def create_note(term: str, result: str, example: str) -> genanki.Note:
    return genanki.Note(model=MODEL, fields=[term, result, example])


def create_deck(notes: list, deck_name: str) -> genanki.Deck:
    deck = genanki.Deck(deck_id=random.randrange(1 << 30, 1 << 31), name=deck_name)
    for note in notes:
        deck.add_note(note)
    return deck


def export_deck(deck: genanki.Deck, deck_name: str):
    package = genanki.Package(deck)
    package.write_to_file(f"{deck_name}.apkg")
    return "Deck was created! No worries"


def generate_anki_deck(data, deck_name: str):
    notes = [create_note(entry.term, entry.result, entry.example) for entry in data]
    deck = create_deck(notes, deck_name)
    return export_deck(deck, deck_name)
