import io
from typing import List, Literal

import genanki
import pandas as pd
from definition_sources.groq_definition import get_groq_definition
from fastapi import FastAPI, File, Form, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from models import VocabularyResponse


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
async def generate_deck(
    content: List[str] | None = Form(None),
    file: UploadFile | None = File(None),
    type: Literal["text", "file"] = Form(...),
    include_pronunciation: bool = Form(...),
    include_picture: bool = Form(...),
    definition_source: Literal["ai", "dictionary", "translation", "corpus", "user"] = Form(...),
    definition_provider: str = Form(...)
):
    return [definition_source, definition_provider]
    if type == "file":
        content = await file.read()
        df = pd.read_csv(io.BytesIO(content))
        words = df.iloc[:, 0].values.tolist()
    else:
        words = content

    cards = []
    vocabulary = get_groq_definition(
        f"These are the words {words}, I want to learn Arabic"
    )

    for entry in vocabulary.entries:
        cards.append((entry.word, entry.meaning))

    create_anki_deck(cards)

    return cards
