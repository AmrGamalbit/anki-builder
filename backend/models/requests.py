from pydantic import BaseModel, Discriminator
from typing import Literal, Annotated


class CSVOptions(BaseModel):
    type: Literal["file"]
    delimiter: str = ","


class TextOptions(BaseModel):
    type: Literal["text"]


class YoutubeOptions(BaseModel):
    type: Literal["youtube"]


class WebOptions(BaseModel):
    type: Literal["web"]


class SourceInput(BaseModel):
    content: str
    options: Annotated[
        CSVOptions, TextOptions, YoutubeOptions, WebOptions, Discriminator("type")
    ]


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
