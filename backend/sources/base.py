from abc import ABC, abstractmethod
from models.responses import UnifiedResponse

class BaseProvider(ABC):

    @abstractmethod
    async def fetch(self, payload: dict) -> dict:
        pass

    @abstractmethod
    def normalize(self, raw: dict) -> UnifiedResponse:
        pass