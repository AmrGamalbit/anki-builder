from typing import List

from pydantic import BaseModel

class VocabularyEntry(BaseModel):
    word: str
    meaning: str
    example: str
    pronunciation: str
    phonetics_text: str

class VocabularyResponse(BaseModel):
    entries: List[VocabularyEntry]
