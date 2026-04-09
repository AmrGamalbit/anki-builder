from pydantic import BaseModel, Discriminator
from typing import Literal, Annotated, Any


class FileOptions(BaseModel):
    type: Literal["file"]
    has_header: bool = False
    word_column: int = 0
    delimiter: str = ","


class TextOptions(BaseModel):
    type: Literal["text"]
    delimiter: str = ","
    strip_punctuation: bool = True
    lowercase: bool = True
    base_form: bool = False


class UrlOptions(BaseModel):
    type: Literal["youtube", "web"]
    vocabulary_level: str
    max_cards: int
    include_idioms: bool


class SourceInput(BaseModel):
    content: Any
    deck_name: str
    options: Annotated[
        FileOptions | TextOptions | UrlOptions, Discriminator("type")
    ] = None


class BaseDeckRequest(BaseModel):
    target_language: str
    include_pronunciation: bool = False
    include_pictogram: bool = False


class DictionaryRequest(BaseDeckRequest):
    use_dictionary_audio: bool = False
    provider: Literal["free_dictionary_api"]


class AIRequest(BaseDeckRequest):
    mode: Literal["definition", "translation"]
    source_language: str
    provider: Literal["gemini", "groq"]


class StyleSettings(BaseModel):
    font_family: str
    font_size: int
    line_height: float
    padding: int
    text_align: str
    accent_color: str
    background_color: str
    color: str
    night_mode: bool


class GenerateRequest(BaseModel):
    source: SourceInput
    deck: Annotated[AIRequest | DictionaryRequest, Discriminator("provider")]
    style: StyleSettings
