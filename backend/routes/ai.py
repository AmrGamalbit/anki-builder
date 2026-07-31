from fastapi import APIRouter, BackgroundTasks, Depends
from core.dispatcher import dispatch
from models.requests import GenerateRequest
from utils.vocabulary import clean_content, get_unusual_words
from models.responses import GenerateResponse
from core.registry import get_provider
from dependencies import get_api_keys
from utils.prompt_builders import build_user_instructions


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
    provider = request.definition_options.provider
    source_language = request.definition_options.source_language
    api_key = api_keys.get(provider)
    terms = clean_content(content, content_options)

    payload = {'user_instructions': build_user_instructions(terms, request.definition_options)}
    ai_response = await dispatch(
        source='ai',
        provider=provider,
        api_key=api_key,
        model=request.definition_options.model,
        payload=payload
    )
    return ai_response


@router.get("/models/{provider}")
def get_available_models(provider: str, api_keys=Depends(get_api_keys)):
    ProviderClass = get_provider("ai", provider)
    instance = ProviderClass(api_key=api_keys.get(provider))
    return instance.get_available_models()
