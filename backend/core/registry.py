from sources.base import BaseProvider
from sources.ai.groq import GroqProvider
from sources.ai.gemini import GeminiProvider
from sources.dictionary.free_dictionary import FreeDictionaryProvider
from sources.dictionary.wordnik import WordnikProvider

REGISTRY = {
    ("ai", "groq"): GroqProvider,
    ("ai", "gemini"): GeminiProvider,
    ("dictionary", "free_dictionary_api"): FreeDictionaryProvider,
    ("dictionary", "wordnik"): WordnikProvider,
}


def get_provider(source: str, provider: str) -> BaseProvider:
    key = (source, provider)
    if key not in REGISTRY:
        raise ValueError(f"Unknown provider: {provider} for source: {source}")
    return REGISTRY[key]
