from fastapi import APIRouter, File, Form, UploadFile
from core.dispatcher import dispatch
from models.requests import AIRequest

router = APIRouter(prefix="/ai", tags=["ai"])

MODE_INSTRUCTIONS = {
    "definition": "provide a clear and simple definition for each term",
    "translation": "translate each term into {target_language}",
}


@router.post("/generate")
async def generate(request: AIRequest):
    terms = request.content.split(",")
    payload = {
        "user_instructions": f"""
        You are given the following terms in {request.source_language}: {terms}

        Your task is to {MODE_INSTRUCTIONS[request.mode].format(target_language=request.target_language)}.
        """
    }

    return await dispatch("ai", request.provider, payload)


@router.post("/generate/upload")
async def generate_from_file(
    file: UploadFile = File(...),
    source_language=Form(...),
    target_language=Form(...),
    include_pronunciation: bool = Form(...),
    include_picture: bool = Form(...),
    definition_provider: str = Form(...),
):
    return "He"
