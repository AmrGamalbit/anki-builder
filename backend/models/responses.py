from .base import BaseSchema


class DefinitionResponse(BaseSchema):
    term: str
    definition: str
    synonyms: list[str] | None = None
    antonyms: list[str] | None = None
    example: str | None = None
    part_of_speech: str
    audio_url: str | None = None
    pictogram_url: str | None = None


class DefinitionsResponse(BaseSchema):
    results: list[DefinitionResponse]


class ExtractedTerm(BaseSchema):
    term: str
    cefr_level: str
    context_sentence: str
    context_clue: str


class ExtractionResponse(BaseSchema):
    terms: list[ExtractedTerm]


class GenerateResponse(BaseSchema):
    source: str
    provider: str
    data: list[DefinitionResponse]
    meta: dict


class CardData(BaseSchema):
    front: str
