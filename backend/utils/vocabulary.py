import string
from utils.prompt_builders import build_extraction_prompt
from nltk.stem import PorterStemmer
from core.dispatcher import dispatch
import json

stemmer = PorterStemmer()


def strip_punctuation(content):
    return content.translate(str.maketrans("", "", string.punctuation))


def convert_to_lowercase(content):
    return content.lower()


def get_base_form(term):
    return stemmer.stem(term)


def clean_content(content, options):
    terms = [term.strip() for term in content.split(options.delimiter)]
    if options.strip_punctuation:
        terms = [strip_punctuation(term) for term in terms]
    if options.lowercase:
        terms = [convert_to_lowercase(term) for term in terms]
    if options.base_form:
        terms = [get_base_form(term) for term in terms]

    return terms


async def get_unusual_words(content, source_language, provider, options):
    user_instructions = build_extraction_prompt(
        content, source_language, provider, options
    )
    payload = {"user_instructions": user_instructions}
    ai_response = json.loads(await dispatch("ai", "groq", payload, normalize=False))
    return ai_response["results"]["terms"]
