from core.registry import get_provider
from sources.base import UnifiedResponse


async def dispatch(
    source: str,
    provider: str,
    model: str,
    api_key: str,
    payload: dict,
    normalize: bool = True,
) -> UnifiedResponse:
    ProviderClass = get_provider(source, provider)
    instance = ProviderClass(api_key)
    raw = await instance.fetch(payload, model)
    if normalize:
        return instance.normalize(raw, model)
    else:
        return raw
