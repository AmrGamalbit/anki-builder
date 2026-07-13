from fastapi import APIRouter, UploadFile, Form, File
from typing import Annotated
from utils.file_parser import handle_file, extract_words

router = APIRouter(prefix="/extract", tags=["file"])


@router.post("/file")
async def extract_from_file(
    file: Annotated[UploadFile, File()],
    type: Annotated[str, Form()],
    word_column: Annotated[int, Form(alias="wordColumn")],
    delimiter: Annotated[str, Form()],
    has_header: Annotated[bool, Form(alias="hasHeader")],
):
    df = await handle_file(file, delimiter, has_header)
    terms = extract_words(df, word_column - 1)
    return ",".join(terms)
