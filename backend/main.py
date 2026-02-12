import genanki
from fastapi import FastAPI


def create_deck(cards):
    new_deck = genanki.Deck(deck_id=123456, name="AnkiBuilder")
    new_model = genanki.Model(
        model_id=554,
        name="SimpleModel",
        fields=[
            {"name": "Question"},
            {"name": "Answer"},
        ],
        templates=[
            {
                "name": "Card 1",
                "qfmt": "{{Question}}",  # Front
                "afmt": '{{FrontSide}}<hr id="answer">{{Answer}}',  # Back
            },
        ],
    )

    for q, a in cards:
        note = genanki.Note(model=new_model, fields=[q, a])
        new_deck.add_note(note)

    genanki.Package(new_deck).write_to_file("AnkiDeck.apkg")

    return "Deck was created! No worries"


app = FastAPI()


@app.get("/")
def index():
    cards = [
        ("People", "More than one person")
    ]
    return create_deck(cards)
