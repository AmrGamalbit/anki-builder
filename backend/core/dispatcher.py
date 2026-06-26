from core.registry import get_provider
from sources.base import UnifiedResponse


async def dispatch(
    source: str, provider: str, model: str, payload: dict, normalize: bool = True
) -> UnifiedResponse:
    ProviderClass = get_provider(source, provider)
    instance = ProviderClass()
    raw = await instance.fetch(payload, model)
    print(raw)
    if normalize:
        return instance.normalize(raw, model)
    else:
        return raw
