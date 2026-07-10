from abc import ABC, abstractmethod
from models.responses import GenerateResponse


class BaseProvider(ABC):
    def __init__(self, api_key: str = None, model: str = None):
        self.api_key = api_key
        self.model = model

    @abstractmethod
    async def fetch(self, payload: dict) -> dict:
        pass

    @abstractmethod
    def normalize(self, raw: dict | list) -> GenerateResponse:
        pass
