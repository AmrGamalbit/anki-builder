from fastapi import APIRouter, Form, UploadFile, File
from typing import Literal
from core.dispatcher import dispatch
from models.requests import AIRequest
from utils.file_parser import handle_file
from services.ai import AIDeckGenerator

router = APIRouter(prefix="/ai", tags=["ai"])

MODE_INSTRUCTIONS = {
    "definition": "provide a clear and simple definition for each term",
    "translation": "translate each term into {target_language}",
}


@router.post("/generate")
async def generate(request: AIRequest):
    terms = request.content.split(",")
    payload = {
        "user_instructions": f"""
        You are given the following terms in {request.source_language}: {terms}

        Your task is to {MODE_INSTRUCTIONS[request.mode].format(target_language=request.target_language)}.
        """
    }

    ai_response = await dispatch("ai", request.provider, payload)
    generator = AIDeckGenerator(
        include_pronunciation=request.include_pronunciation,
        include_pictogram=request.include_pictures,
        target_language=request.target_language,
    )
    generator.include_pictures = request.include_pictures
    return await generator.export_deck("MY ULTIMATE DECK", ai_response.data)


@router.post("/generate/upload")
async def generate_from_file(
    content: UploadFile = File(description="The file must be a text file"),
    mode: Literal["definition", "translation"] = Form(...),
    source_language: str = Form(...),
    target_language: str = Form(...),
    include_pronunciation: bool = Form(...),
    include_pictures: bool = Form(...),
    provider: str = Form(...),
):
    df = await handle_file(content)
    terms = df.iloc[:, 0].values.tolist()
    payload = {
        "user_instructions": f"""
        You are given the following terms in {source_language}: {terms}

        Your task is to {MODE_INSTRUCTIONS[mode].format(target_language=target_language)}.
        """
    }
    ai_response = await dispatch("ai", provider, payload)
    generator = AIDeckGenerator()
    generator = AIDeckGenerator(
        include_pronunciation=include_pronunciation,
        include_pictogram=include_pictures,
        target_language=target_language,
    )
    return await generator.export_deck(ai_response.data, "Help me AI")
