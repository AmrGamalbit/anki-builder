from core.registry import get_provider
from models.responses import GenerateResponse


async def dispatch(
    source: str,
    provider: str,
    payload: dict,
    api_key: str = None,
    model: str = None,
    normalize: bool = True,
) -> GenerateResponse:
    ProviderClass = get_provider(source, provider)
    instance = ProviderClass(api_key, model)
    raw = await instance.fetch(payload)
    if normalize:
        return instance.normalize(raw)
    else:
        return raw
