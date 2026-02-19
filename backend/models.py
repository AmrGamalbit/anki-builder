from pydantic import BaseModel
from typing import List, Literal

class GenerateRequest(BaseModel):
    words: List[str]
    include_ponunciation: bool
    include_photos: bool
    definition_source: Literal["ai", "dictionary", "translation", "corpus", "user"]
