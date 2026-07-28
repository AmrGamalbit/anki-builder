from abc import ABC, abstractmethod
from models.responses import GenerateResponse
from models.requests import CardFields


class BaseProvider(ABC):
    def __init__(self, api_key: str = None, model: str = None, card_fields: CardFields = None):
        self.api_key = api_key
        self.model = model
        self.card_fields = card_fields

    @abstractmethod
    async def fetch(self, payload: dict) -> dict:
        pass

    @abstractmethod
    def normalize(self, raw: dict | list) -> GenerateResponse:
        pass
