from fastapi import APIRouter, BackgroundTasks
from core.dispatcher import dispatch
from models.requests import GenerateRequest
from services.dictionary import DictionaryDeckGenerator
from services.youtube import get_transcript
from services.web import extract_article
from utils.vocabulary import clean_content, get_unusual_words

router = APIRouter(prefix="/dictionary", tags=["dictionary"])


@router.post("/lookup")
async def lookup(request: GenerateRequest, background_tasks: BackgroundTasks):
    content = request.content
    content_type = request.content_type
    content_options = request.content_options
    provider = request.definition_options.provider
    if content_type == "youtube":
        content = get_transcript(content)
        terms = await get_unusual_words(content, "en", provider, content_options)
    elif content_type == "web":
        content = extract_article(content)
        terms = await get_unusual_words(content, "en", provider, content_options)
    else:
        terms = clean_content(content, content_options)

    payload = {"words": terms}
    dictionary_response = await dispatch("dictionary", provider, payload)
    generator = DictionaryDeckGenerator(
        include_pronunciation=request.definition_options.include_pronunciation,
        include_pictogram=request.definition_options.include_pictogram,
        target_language=request.definition_options.target_language,
        use_dictionary_audio=request.definition_options.use_dictionary_audio,
        style=request.appearance_options,
    )
    return await generator.export_deck(
        dictionary_response.data, request.deck_name, background_tasks
    )
