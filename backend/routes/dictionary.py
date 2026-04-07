from fastapi import APIRouter, Form, UploadFile, File, HTTPException
from typing import Literal
from core.dispatcher import dispatch
from models.requests import GenerateRequest
from utils.file_parser import handle_file
from services.dictionary import DictionaryDeckGenerator

router = APIRouter(prefix="/dictionary", tags=["dictionary"])

MODE_INSTRUCTIONS = {
    "definition": "provide a clear and simple definition for each term",
    "translation": "translate each term into {target_language}",
}


@router.post("/lookup")
async def generate(request: GenerateRequest):
    deck, source, style = request.deck, request.source, request.style
    terms = request.source.content.split(source.options.delimiter)
    payload = {"words": terms}
    dictionary_response = await dispatch("dictionary", deck.provider, payload)
    generator = DictionaryDeckGenerator(
        include_pronunciation=deck.include_pronunciation,
        include_pictogram=deck.include_pictogram,
        target_language=deck.target_language,
        use_dictionary_audio=deck.use_dictionary_audio,
        style=style,
    )
    return await generator.export_deck(dictionary_response.data, source.deck_name)


@router.post("/lookup/upload")
async def generate_from_file(
    content: UploadFile = File(description="The file must be a text file"),
    target_language: str = Form(...),
    include_pronunciation: bool = Form(...),
    include_pictures: bool = Form(...),
    use_dictionary_audio: bool = Form(...),
    provider: Literal["free_dictionary_api"] = Form(...),
):
    df = await handle_file(content)
    terms = df.iloc[:, 0].values.tolist()
    payload = {"words": terms}
    dictionary_response = await dispatch("dictionary", provider, payload)
    generator = DictionaryDeckGenerator(
        include_pronunciation=include_pronunciation,
        include_pictogram=include_pictures,
        target_language=target_language,
        use_dictionary_audio=use_dictionary_audio,
    )
    return await generator.export_deck(dictionary_response.data, "HELP me dict")
