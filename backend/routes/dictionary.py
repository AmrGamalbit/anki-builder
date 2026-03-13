from fastapi import APIRouter, Form, UploadFile, File
from typing import Literal
from core.dispatcher import dispatch
from models.requests import DictionaryRequest
from utils.file_parser import handle_file
from services.anki import DictionaryDeckGenerator

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
    generator = DictionaryDeckGenerator()
    generator.build(dictionary_response.data, "Help me Dict")
    return generator.export_deck()


@router.post("/generate/upload")
async def generate_from_file(
    file: UploadFile = File(description="The file must be a text file"),
    include_pronunciation: bool = Form(...),
    include_picture: bool = Form(...),
    provider: Literal["free_dictionary_api"] = Form(...),
):
    df = await handle_file(file)
    terms = df.iloc[:, 0].values.tolist()
    payload = {"words": terms}
    dictionary_response = await dispatch("dictionary", provider, payload)
    generator = DictionaryDeckGenerator()
    generator.build(dictionary_response.data, "Help me Dict")
    return generator.export_deck()
