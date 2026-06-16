from fastapi import APIRouter, BackgroundTasks
from core.dispatcher import dispatch
from models.requests import GenerateRequest
from services.youtube import get_transcript
from services.web import extract_article
from utils.prompt_builders import build_anki_prompt
from utils.vocabulary import clean_content, get_unusual_words
from models.responses import CardData, GenerateResponse

router = APIRouter(prefix="/ai", tags=["ai"])


@router.post("/generate")
async def generate(request: GenerateRequest, background_tasks: BackgroundTasks):
    content = request.content
    content_type = request.content_type
    content_options = request.content_options
    definition_options = request.definition_options
    provider = definition_options.provider
    source_language = definition_options.source_language
    target_language = definition_options.target_language
    mode = definition_options.mode

    if content_type == "youtube":
        content = get_transcript(content)
        terms = await get_unusual_words(
            content,
            source_language,
            provider,
            content_options,
        )
    elif content_type == "web":
        content = extract_article(content)
        terms = await get_unusual_words(
            content, source_language, provider, content_options
        )
    else:
        terms = clean_content(content, content_options)

    user_instructions = build_anki_prompt(
        terms,
        source_language,
        mode,
        content_options,
        target_language,
    )
    payload = {"user_instructions": user_instructions}
    ai_response = await dispatch("ai", provider, payload)
    cards = [
        CardData(term=card.term, front=card.term, back=card.result)
        for card in ai_response.data
    ]
    return GenerateResponse(cards=cards)
