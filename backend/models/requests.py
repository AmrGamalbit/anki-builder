from pydantic import BaseModel, Discriminator, model_validator, ConfigDict
from pydantic.alias_generators import to_camel
from typing import Literal, Annotated, Any
from .responses import CardData


class BaseSchema(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        from_attributes=True,
    )


class FileOptions(BaseSchema):
    type: Literal["file"]
    has_header: bool = False
    word_column: int = 0
    delimiter: str = ","
    strip_punctuation: bool = True
    lowercase: bool = True
    base_form: bool = False


class TextOptions(BaseSchema):
    type: Literal["text"]
    delimiter: str = ","
    strip_punctuation: bool = True
    lowercase: bool = True
    base_form: bool = False


class UrlOptions(BaseSchema):
    type: Literal["youtube", "web"]
    vocabulary_level: str
    max_cards: int
    include_idioms: bool


class DefinitionOptions(BaseSchema):
    source_language: str
    target_language: str
    include_pronunciation: bool = False
    include_pictogram: bool = False


class DictionaryOptions(DefinitionOptions):
    source: Literal["dictionary"]
    use_dictionary_audio: bool = False
    provider: Literal["free_dictionary_api"]


class AIOptions(DefinitionOptions):
    source: Literal["ai"]
    mode: Literal["definition", "translation"]
    model: str
    source_language: str
    provider: Literal["gemini", "groq"]


class AppearanceOptions(BaseSchema):
    font_family: str
    font_size: int
    line_height: float
    padding: int
    text_align: str
    accent_color: str
    background_color: str
    color: str
    night_mode: bool


class GenerateRequest(BaseSchema):
    content: str
    content_type: str
    content_options: Annotated[
        FileOptions | TextOptions | UrlOptions, Discriminator("type")
    ] = None
    appearance_options: AppearanceOptions
    definition_options: Annotated[
        AIOptions | DictionaryOptions, Discriminator("source")
    ]

    @model_validator(mode="before")
    @classmethod
    def inject_type(cls, data: Any):
        content_options = data.get("contentOptions")
        content_type = data.get("contentType")
        if isinstance(content_options, dict):
            content_options["type"] = content_type
        return data


class ExportRequest(BaseSchema):
    data: list[CardData]
    pronunciation_urls: dict[str, str] = {}
    appearance_options: AppearanceOptions
    definition_options: Annotated[
        AIOptions | DictionaryOptions, Discriminator("source")
    ]
    deck_name: str


class ApiKeysRequest(BaseSchema):
    groq: str | None = None
    gemini: str | None = None
