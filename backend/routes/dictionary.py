from fastapi import APIRouter, BackgroundTasks, Depends
from core.dispatcher import dispatch
from models.requests import GenerateRequest
from models.responses import GenerateResponse
from utils.vocabulary import clean_content, get_unusual_words
from dependencies import get_api_keys


router = APIRouter(prefix="/dictionary", tags=["dictionary"])


@router.post("/lookup")
async def lookup(
    request: GenerateRequest,
    background_tasks: BackgroundTasks,
    api_keys=Depends(get_api_keys),
) -> GenerateResponse:
    content = request.content
    content_options = request.content_options
    provider = request.definition_options.provider
    api_key = api_keys.get(provider)
    terms = clean_content(content, content_options)
    payload = {"terms": terms, "card_fields": request.definition_options.card_fields}
    dictionary_response = await dispatch(
        source="dictionary", provider=provider, api_key=api_key, payload=payload
    )
    return dictionary_response
