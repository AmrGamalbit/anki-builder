from fastapi import APIRouter
from core.dispatcher import dispatch
from models.requests import GenerateRequest
from services.ai import AIDeckGenerator
from services.youtube import get_transcript
from utils.prompt_builders import build_user_instructions

router = APIRouter(prefix="/ai", tags=["ai"])


@router.post("/generate")
async def generate(request: GenerateRequest):
    deck, source, style = request.deck, request.source, request.style

    if source.options.type == "youtube":
        content = get_transcript(source.content)
        content_type = "transcript"

    else:
        content = source.content
        content_type = "terms"
    payload = {
        "user_instructions": build_user_instructions(
            content,
            deck.source_language,
            deck.mode,
            content_type,
            source.options,
            deck.target_language,
        )
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
