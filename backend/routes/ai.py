from fastapi import APIRouter, Form, UploadFile, File, HTTPException
from typing import Literal
from core.dispatcher import dispatch
from models.requests import GenerateRequest
from utils.file_parser import handle_file
from services.ai import AIDeckGenerator

router = APIRouter(prefix="/ai", tags=["ai"])

MODE_INSTRUCTIONS = {
    "definition": "provide a clear and simple definition for each term",
    "translation": "translate each term into {target_language}",
}


@router.post("/generate")
async def generate(request: GenerateRequest):
    deck, source, style = request.deck, request.source, request.style
    terms = source.content.split(source.options.delimiter)
    payload = {
        "user_instructions": f"""
        You are given the following terms in {deck.source_language}: {terms}

        Your task is to {MODE_INSTRUCTIONS[deck.mode].format(target_language=deck.target_language)}.
        """
    }

    try:
        ai_response = await dispatch("ai", deck.provider, payload)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    generator = AIDeckGenerator(
        include_pronunciation=deck.include_pronunciation,
        include_pictogram=deck.include_pictogram,
        target_language=deck.target_language,
        style=style,
    )

    return await generator.export_deck(ai_response.data, request.source.deck_name)


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
    try:
        ai_response = await dispatch("ai", provider, payload)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    generator = AIDeckGenerator(
        include_pronunciation=include_pronunciation,
        include_pictogram=include_pictures,
        target_language=target_language,
    )
    return await generator.export_deck(ai_response.data, "Help me AI")
