from pydantic import BaseModel
from typing import Literal


class AIRequest(BaseModel):
    content: str
    mode: Literal["definition", "translation"]
    source_language: str
    target_language: str
    provider: str
