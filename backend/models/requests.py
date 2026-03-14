from pydantic import BaseModel
from typing import Literal


class DictionaryRequest(BaseModel):
    content: str
    include_pronunciation: bool = False
    provider: Literal["free_dictionary_api"]


class AIRequest(BaseModel):
    content: str
    mode: Literal["definition", "translation"]
    source_language: str
    target_language: str
    include_pronunciation: bool = False
    provider: Literal["gemini", "groq"]
