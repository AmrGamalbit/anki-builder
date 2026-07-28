from sources.base import BaseProvider
from models.responses import GenerateResponse, DefinitionResponse
import asyncio
import aiohttp

BASE_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/{word}"


class FreeDictionaryProvider(BaseProvider):
    async def fetch(self, payload):
        urls = [BASE_URL.format(word=word) for word in payload.get("terms")]
        async with aiohttp.ClientSession() as session:

            async def fetch_one(url):
                try:
                    async with session.get(url) as response:
                        response.raise_for_status()
                        return await response.json()
                except aiohttp.ClientError as e:
                    print(f"Error fetching data from {url}: {e}")
                    return None
                except asyncio.TimeoutError:
                    print(f"Request to {url} timed out")
                    return None

            responses = await asyncio.gather(*[fetch_one(url) for url in urls])
        responses = [response for response in responses if response is not None]
        return responses

    def normalize(self, raw):
        data = []
        for response in raw:
            for entry in response:
                audio_url = next(
                    (p.get("audio") for p in entry.get("phonetics") if p.get("audio")),
                    None,
                )
                for meaning in entry.get("meanings"):
                    for definition in meaning.get("definitions")[:2]:
                        data.append(
                            DefinitionResponse(
                                term=entry.get("word"),
                                definition=definition.get("definition"),
                                synonyms=definition.get("synonyms")
                                if self.card_fields.synonyms
                                else None,
                                antonyms=definition.get("antonyms")
                                if self.card_fields.antonyms
                                else None,
                                example=definition.get("example")
                                if self.card_fields.example
                                else None,
                                part_of_speech=meaning.get("partOfSpeech")
                                if self.card_fields.part_of_speech
                                else None,
                                audio_url=audio_url if self.card_fields.audio else None,
                            )
                        )
        meta = {"total": len(raw)}
        return GenerateResponse(
            source="dictionary", provider="free", data=data, meta=meta
        )
