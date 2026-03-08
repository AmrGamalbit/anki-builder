from sources.ai.groq import GroqProvider
from sources.ai.gemini import GeminiProvider
from sources.base import BaseProvider

REGISTRY = {("ai", "groq"): GroqProvider, ("ai", "gemini"): GeminiProvider}


def get_provider(source: str, provider: str) -> BaseProvider:
    key = (source, provider)
    if key not in REGISTRY:
        raise ValueError(f"Unknown provider: {provider} for source: {source}")
    return REGISTRY[key]
