from fastapi import APIRouter, Request
from models.requests import ApiKeysRequest

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/apikeys")
async def save_api_keys(request: Request, body: ApiKeysRequest):
    for provider, key in body.model_dump().items():
        cleaned_key = key.strip() if isinstance(key, str) else key
        if cleaned_key:
            request.session[provider] = cleaned_key
    return {"status": "success", "saved_providers": list(request.session.keys())}
