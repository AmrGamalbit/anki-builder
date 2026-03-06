from pydantic import BaseModel
from typing import Any, Union


class AIResponseData(BaseModel):
    term: str
    result: str
    example: str


class AIResponse(BaseModel):
    results: list[AIResponseData]


class DictionaryData(BaseModel):
    word: str
    definitions: list[str]
    examples: list[str]
    synonyms: list[str]


class UnifiedResponse(BaseModel):
    source: str
    provider: str
    data: list[Union[DictionaryData, AIResponseData]]
    meta: dict
