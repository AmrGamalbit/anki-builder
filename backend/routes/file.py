from fastapi import APIRouter, UploadFile, Form, File
from typing import Annotated
from utils.file_parser import handle_file, extract_words

router = APIRouter(prefix="/file", tags=["file"])


@router.post("/extract")
async def generate(
    file: Annotated[UploadFile, File()],
    type: Annotated[str, Form()],
    word_column: Annotated[int, Form()],
    delimiter: Annotated[str, Form()],
    has_header: Annotated[bool, Form()],
):
    df = await handle_file(file, delimiter, has_header)
    terms = extract_words(df, word_column - 1)
    return ",".join(terms)
