from fastapi import APIRouter
from core.dispatcher import dispatch
from models.requests import GenerateRequest
from services.dictionary import DictionaryDeckGenerator
from utils.file_parser import handle_file, extract_words

router = APIRouter(prefix="/dictionary", tags=["dictionary"])

MODE_INSTRUCTIONS = {
    "definition": "provide a clear and simple definition for each term",
    "translation": "translate each term into {target_language}",
}


@router.post("/lookup")
async def generate(request: GenerateRequest):
    deck, source, style = request.deck, request.source, request.style
    terms = request.source.content.split(source.options.delimiter)
    payload = {"words": terms}
    dictionary_response = await dispatch("dictionary", deck.provider, payload)
    generator = DictionaryDeckGenerator(
        include_pronunciation=deck.include_pronunciation,
        include_pictogram=deck.include_pictogram,
        target_language=deck.target_language,
        use_dictionary_audio=deck.use_dictionary_audio,
        style=style,
    )
    return await generator.export_deck(dictionary_response.data, source.deck_name)
