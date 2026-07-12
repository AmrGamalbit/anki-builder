from fastapi import APIRouter, BackgroundTasks, Depends
from core.dispatcher import dispatch
from models.requests import GenerateRequest
from models.responses import GenerateResponse
from services.youtube import get_transcript
from services.web import extract_article
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
    content_type = request.content_type
    content_options = request.content_options
    provider = request.definition_options.provider
    api_key = api_keys.get(provider)

    if content_type == "youtube":
        content = get_transcript(content)
        terms = await get_unusual_words(content, "en", provider, content_options)
    elif content_type == "web":
        content = extract_article(content)
        terms = await get_unusual_words(content, "en", provider, content_options)
    else:
        terms = clean_content(content, content_options)

    payload = {"words": terms}
    dictionary_response = await dispatch("dictionary", provider, payload, api_key)
    return dictionary_response
