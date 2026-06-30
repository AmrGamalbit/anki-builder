from fastapi import APIRouter, Request
from models.requests import ApiKeysRequest

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/apikeys")
async def save_api_keys(request: Request, body: ApiKeysRequest):
    for provider, key in body.model_dump().items():
        if key:
            request.session[provider] = key
    return {"status": "success", "saved_providers": list(body.model_dump().keys())}
