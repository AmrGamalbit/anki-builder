from fastapi import UploadFile
import pandas as pd
import io


async def parse_csv(file: UploadFile):
    try:
        content = await file.read()
        df = pd.read_csv(io.BytesIO(content))
        return df

    except pd.errors.EmptyDataError:
        raise ValueError("CSV file is empty")

    except pd.errors.ParserError:
        raise ValueError("Invalid CSV file")


def prase_excel():
    pass


FILE_HANDLERS = {"csv": parse_csv, "xlsx": prase_excel}


async def get_file_handler(file: UploadFile):
    filename = file.filename
    file_type = filename.split(".")[-1]
    if file_type not in FILE_HANDLERS:
        raise ValueError(f"Unsupported file type: {file_type}")
    return FILE_HANDLERS[file_type]


async def handle_file(file: UploadFile):
    handler = await get_file_handler(file)
    return await handler(file)
