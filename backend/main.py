import genanki
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import GenerateRequest


def create_anki_deck(cards):
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

origins = ["http://localhost:5173"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def index():
    return "Server is running!"


@app.post("/generate-deck")
def generate_deck(data: GenerateRequest):
    cards = [("People", "More than one person")]
    return data.words
    # return create_anki_deck(cards)
