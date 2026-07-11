from fastapi import APIRouter, BackgroundTasks, Depends
from core.dispatcher import dispatch
from models.requests import GenerateRequest
from services.youtube import get_transcript
from services.web import extract_article
from utils.prompt_builders import build_anki_prompt
from utils.vocabulary import clean_content, get_unusual_words
from models.responses import GenerateResponse
from core.registry import get_provider
from dependencies import get_api_keys

router = APIRouter(prefix="/ai", tags=["ai"])


@router.post("/generate")
async def generate(
    request: GenerateRequest,
    background_tasks: BackgroundTasks,
    api_keys=Depends(get_api_keys),
) -> GenerateResponse:
    content = request.content
    content_type = request.content_type
    content_options = request.content_options
    definition_options = request.definition_options
    provider = definition_options.provider
    source_language = definition_options.source_language
    target_language = definition_options.target_language
    mode = definition_options.mode
    model = definition_options.model
    api_key = api_keys.get(provider)

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
    ai_response = await dispatch(
        source="ai", provider=provider, model=model, api_key=api_key, payload=payload
    )
    return ai_response


@router.get("/models/{provider}")
def get_available_models(provider: str, api_keys=Depends(get_api_keys)):
    ProviderClass = get_provider("ai", provider)
    instance = ProviderClass(api_key=api_keys.get(provider))
    return instance.get_available_models()
