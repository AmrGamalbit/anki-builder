from pydantic import BaseModel


class DefinitionResponse(BaseModel):
    term: str
    definition: str
    synonyms: list[str] | None = None
    antonyms: list[str] | None = None
    example: str | None = None
    part_of_speech: str
    audio_url: str | None = None
    pictogram_url: str | None = None


class DefinitionsResponse(BaseModel):
    results: list[DefinitionResponse]


class ExtractedTerm(BaseModel):
    term: str
    cefr_level: str
    context_sentence: str
    context_clue: str


class ExtractionResponse(BaseModel):
    terms: list[ExtractedTerm]


class GenerateResponse(BaseModel):
    source: str
    provider: str
    data: list[DefinitionResponse]
    meta: dict


class CardData(BaseModel):
    front: str
