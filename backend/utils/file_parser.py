from fastapi import UploadFile
import pandas as pd
import io


async def parse_csv(file: UploadFile, delimiter: str, has_header: bool):
    try:
        content = await file.read()
        header = 0 if has_header else None
        df = pd.read_csv(io.BytesIO(content), sep=delimiter, header=header)
        return df

    except pd.errors.EmptyDataError:
        raise ValueError("CSV file is empty")

    except pd.errors.ParserError:
        raise ValueError("Invalid CSV file")


async def parse_excel(file: UploadFile, has_header: bool):
    try:
        content = await file.read()
        header = 0 if has_header else None
        df = pd.read_excel(io.BytesIO(content), header=header)
        return df

    except pd.errors.EmptyDataError:
        raise ValueError("Excel file is empty")

    except pd.errors.ParserError:
        raise ValueError("Invalid Excel file")


FILE_HANDLERS = {"csv": parse_csv, "xlsx": parse_excel}


async def get_file_handler(file: UploadFile):
    filename = file.filename
    file_type = filename.split(".")[-1]
    if file_type not in FILE_HANDLERS:
        raise ValueError(f"Unsupported file type: {file_type}")
    return FILE_HANDLERS[file_type]


async def handle_file(file: UploadFile, delimiter: str, has_header: bool):
    handler = await get_file_handler(file)
    return await handler(file, delimiter, has_header)


def extract_words(df, word_column):
    terms = df.iloc[:, word_column].values.tolist()
    return terms
