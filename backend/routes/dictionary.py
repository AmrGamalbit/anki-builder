from fastapi import APIRouter, BackgroundTasks
from core.dispatcher import dispatch
from models.requests import GenerateRequest
from services.dictionary import DictionaryDeckGenerator
from services.youtube import get_transcript
from services.web import extract_article
from utils.vocabulary import clean_content, get_unusual_words
from utils.file_parser import handle_file, extract_words

router = APIRouter(prefix="/dictionary", tags=["dictionary"])

MODE_INSTRUCTIONS = {
    "definition": "provide a clear and simple definition for each term",
    "translation": "translate each term into {target_language}",
}


@router.post("/lookup")
async def generate(request: GenerateRequest, background_tasks: BackgroundTasks):
    deck, source, style = request.deck, request.source, request.style
    if source.options.type == "youtube":
        content = get_transcript(source.content)
        terms = await get_unusual_words(content, "en", deck.provider, source.options)
    elif source.options.type == "web":
        content = extract_article(source.content)
        terms = await get_unusual_words(content, "en", deck.provider, source.options)
    else:
        print(source.options)
        terms = clean_content(source.content, source.options)

    payload = {"words": terms}
    dictionary_response = await dispatch("dictionary", deck.provider, payload)
    generator = DictionaryDeckGenerator(
        include_pronunciation=deck.include_pronunciation,
        include_pictogram=deck.include_pictogram,
        target_language=deck.target_language,
        use_dictionary_audio=deck.use_dictionary_audio,
        style=style,
    )
    return await generator.export_deck(
        dictionary_response.data, source.deck_name, background_tasks
    )
