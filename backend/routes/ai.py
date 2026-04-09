from fastapi import APIRouter
from core.dispatcher import dispatch
from models.requests import GenerateRequest
from services.ai import AIDeckGenerator
from utils.file_parser import handle_file, extract_words

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

    ai_response = await dispatch("ai", deck.provider, payload)
    generator = AIDeckGenerator(
        include_pronunciation=deck.include_pronunciation,
        include_pictogram=deck.include_pictogram,
        target_language=deck.target_language,
        mode=deck.mode,
        style=style,
    )

    return await generator.export_deck(ai_response.data, source.deck_name)
