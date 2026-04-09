from pydantic import BaseModel
from typing import Any, Union


class Definition(BaseModel):
    text: str
    synonyms: list[str] | None = None
    antonyms: list[str] | None = None
    example: str | None = None


class Meaning(BaseModel):
    part_of_speech: str
    definitions: list[Definition]


class DictionaryEntry(BaseModel):
    term: str
    pronunciation: str | None = None
    meanings: list[Meaning]


class DictionaryResponse(BaseModel):
    results: list[DictionaryEntry]


class ExtractedTerms(BaseModel):
    terms: list[str]


class AIResponseData(BaseModel):
    term: str
    result: str
    example: str


class AIResponse(BaseModel):
    results: list[AIResponseData] | ExtractedTerms


class UnifiedResponse(BaseModel):
    source: str
    provider: str
    data: list[Union[DictionaryEntry, AIResponseData]]
    meta: dict
