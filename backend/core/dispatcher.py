from core.registry import get_provider
from sources.base import UnifiedResponse


async def dispatch(
    source: str, provider: str, payload: dict, normalize: bool = True
) -> UnifiedResponse:
    ProviderClass = get_provider(source, provider)
    instance = ProviderClass()
    raw = await instance.fetch(payload)
    if normalize:
        return instance.normalize(raw)
    else:
        return raw
