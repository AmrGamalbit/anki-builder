from sources.base import BaseProvider
from models.responses import GenerateResponse, DefinitionResponse
import asyncio
import aiohttp

BASE_URL = "http://api.wordnik.com/v4/word.json/{word}"


class WordnikProvider(BaseProvider):
    def __init__(self, api_key: str, model: str | None):
        super().__init__(api_key)
        self.endpoints_config = {
            "definitions": {
                "api_key": self.api_key,
                "limit": 10,
                "sourceDictionaries": "ahd-5",
            },
            "topExample": {"api_key": self.api_key},
            "audio": {"api_key": self.api_key, "limit": 1},
        }

    async def _fetch_url(self, url, session, params=None):
        try:
            async with session.get(url, params=params) as response:
                response.raise_for_status()
                return await response.json()
        except aiohttp.ClientError as e:
            print(f"Error fetching data from {url}: {e}")
            return None
        except asyncio.TimeoutError:
            print(f"Request to {url} timed out")
            return None

    async def _fetch_word(self, word, session):
        responses = await asyncio.gather(
            *[
                self._fetch_url(
                    f"{BASE_URL.format(word=word)}/{endpoint}", session, params
                )
                for endpoint, params in self.endpoints_config.items()
            ]
        )
        result = dict(zip(self.endpoints_config.keys(), responses))
        return result

    async def fetch(self, payload, model=None):
        async with aiohttp.ClientSession() as session:
            responses = await asyncio.gather(
                *[self._fetch_word(word, session) for word in payload.get("words")]
            )
        responses = [response for response in responses if response is not None]
        return responses

    def normalize(self, raw, model=None):
        data = []
        for response in raw:
            for definition in response.get("definitions"):
                if definition.get("text"):
                    data.append(
                        DefinitionResponse(
                            term=definition.get("word"),
                            definition=definition.get("text"),
                            example=response.get("topExample").get("text"),
                            part_of_speech=definition.get("partOfSpeech"),
                            audio_url=response.get("audio")[0].get("fileUrl"),
                        )
                    )
        meta = {"total": len(raw)}
        return GenerateResponse(
            source="dictionary", provider="wordnik", data=data, meta=meta
        )
