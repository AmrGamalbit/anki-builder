from fastapi import APIRouter, Form, UploadFile, File
from typing import Literal
from core.dispatcher import dispatch
from models.requests import DictionaryRequest
from utils.file_parser import handle_file
from services.dictionary import DictionaryDeckGenerator

router = APIRouter(prefix="/dictionary", tags=["dictionary"])

MODE_INSTRUCTIONS = {
    "definition": "provide a clear and simple definition for each term",
    "translation": "translate each term into {target_language}",
}


@router.post("/lookup")
async def generate(request: DictionaryRequest):
    terms = request.content.split(",")
    payload = {"words": terms}

    dictionary_response = await dispatch("dictionary", request.provider, payload)
    generator = DictionaryDeckGenerator(
        include_pronunciation=request.include_pronunciation,
        include_pictogram=request.include_pictures,
        target_language=request.target_language,
        use_dictionary_audio=request.use_dictionary_audio,
    )
    generator.use_dictionary_audio = request.use_dictionary_audio
    generator.lang = request.target_language
    return await generator.export_deck(dictionary_response.data, "Help me Dict")


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
