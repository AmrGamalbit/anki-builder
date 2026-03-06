import io
from typing import List, Literal

import genanki
import pandas as pd
from definition_sources.groq_definition import get_groq_definition
from definition_sources.free_dictionary import fetch_data
from fastapi import FastAPI, File, Form, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from models import VocabularyResponse


def create_anki_deck(cards: tuple, media_files: list = None):
    new_deck = genanki.Deck(deck_id=123456, name="AnkiBuilder")
    new_model = genanki.Model(
        model_id=554,
        name="SimpleModel",
        fields=[
            {"name": "Question"},
            {"name": "Answer"},
            {"name": "Audio"}
        ],
        templates=[
            {
                "name": "Card 1",
                "qfmt": "{{Question}}",  # Front
                "afmt": '{{FrontSide}}<hr id="answer">{{Answer}}{{Audio}}',  # Back
            },
        ],
    )

    for question, answer, audio in cards:
        note = genanki.Note(model=new_model, fields=[question, answer, audio])
        new_deck.add_note(note)

    package = genanki.Package(new_deck)
    if media_files:
        package.media_files = media_files
    package.write_to_file("AnkiDeck.apkg")
    return "Deck was created! No worries"

def prepare_cards(entries):
    cards = []
    for entry in entries:
        cards.append(entry.word, entry.meaning)
    return cards

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
    source_language = Form(...),
    target_language = Form(...),
    include_pronunciation: bool = Form(...),
    include_picture: bool = Form(...),
    definition_source: Literal["ai", "dictionary", "translation", "corpus", "user"] = Form(...),
    definition_provider: str = Form(...)
):
    if type == "file":
        content = await file.read()
        df = pd.read_csv(io.BytesIO(content))
        words = df.iloc[:, 0].values.tolist()
    else:
        words = content

    if definition_source == "ai":
        if definition_provider == "groq":
            vocabulary = get_groq_definition(
                f"These are the words {words}, I want to learn Arabic"
            )
            cards = prepare_cards(vocabulary.entries)
    else:
        cards = prepare_cards(fetch_data)

    create_anki_deck(cards)
    return cards
