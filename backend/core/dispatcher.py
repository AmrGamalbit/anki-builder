from core.registry import get_provider
from models.responses import GenerateResponse


async def dispatch(
    source: str,
    provider: str,
    api_key: str,
    payload: dict,
    model: str | None = None,
    normalize: bool = True,
) -> GenerateResponse:
    ProviderClass = get_provider(source, provider)
    instance = ProviderClass(api_key=api_key, model=model, card_fields=payload.get('card_fields'))
    raw = await instance.fetch(payload)
    if normalize:
        return instance.normalize(raw)
    else:
        return raw
