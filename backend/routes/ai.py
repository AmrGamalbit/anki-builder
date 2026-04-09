from fastapi import APIRouter
from core.dispatcher import dispatch
from models.requests import GenerateRequest
from services.ai import AIDeckGenerator
from services.youtube import get_transcript
from utils.prompt_builders import build_anki_prompt
from utils.vocabulary import clean_content, get_unusual_words

router = APIRouter(prefix="/ai", tags=["ai"])


@router.post("/generate")
async def generate(request: GenerateRequest):
    deck, source, style = request.deck, request.source, request.style

    if source.options.type == "youtube":
        content = get_transcript(source.content)
        terms = await get_unusual_words(
            content, deck.source_language, deck.provider, source.options
        )

    else:
        terms = clean_content(source.content, source.options)
    user_instructions = build_anki_prompt(
        terms, deck.source_language, deck.mode, source.options, deck.target_language
    )
    payload = {"user_instructions": user_instructions}
    ai_response = await dispatch("ai", deck.provider, payload)
    generator = AIDeckGenerator(
        include_pronunciation=deck.include_pronunciation,
        include_pictogram=deck.include_pictogram,
        target_language=deck.target_language,
        mode=deck.mode,
        style=style,
    )

    return await generator.export_deck(ai_response.data, source.deck_name)
