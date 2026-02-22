from pydantic import BaseModel
from typing import List, Literal
from fastapi import UploadFile, Form, File

class GenerateRequest(BaseModel):
    content: List[str] | None
    file: UploadFile | None
    type: Literal["text", "file"]
    include_pronunciation: bool
    include_photos: bool
    definition_source: Literal["ai", "dictionary", "translation", "corpus", "user"]

class VocabularyEntry(BaseModel):
    word: str
    meaning: str
    example: str

class VocabularyResponse(BaseModel):
    entries: List[VocabularyEntry]
