from sources.base import BaseProvider
from models.responses import UnifiedResponse, Definition, Meaning, DictionaryEntry
import asyncio
import aiohttp

BASE_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/{word}"


class FreeDictionaryProvider(BaseProvider):
    async def fetch(self, payload):
        urls = [BASE_URL.format(word=word) for word in payload.get("words")]
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
        entries = []
        for response in raw:
            for entry in response:
                term = entry.get("word")
                meanings = []
                for meaning in entry.get("meanings"):
                    definitions = []
                    for definition in meaning.get("definitions")[:2]:
                        definitions.append(
                            Definition(
                                text=definition.get("definition"),
                                synonyms=definition.get("synonyms"),
                                antonyms=definition.get("antonyms"),
                                example=definition.get("example"),
                            )
                        )
                    meanings.append(
                        Meaning(
                            part_of_speech=meaning.get("partOfSpeech"),
                            definitions=definitions,
                        )
                    )
                entries.append(DictionaryEntry(term=term, meanings=meanings))

        # word_definitions = []
        # for record in raw:
        #     meanings_by_pos = {}
        #     entry = record[0]
        #     term = entry.get("word")
        #     meanings_by_pos["term"] = term
        #     for meaning in entry.get("meanings", []):
        #         pos = meaning.get("partOfSpeech")
        #         definitions = meaning.get("definitions", [])
        #         first_definition = (
        #             definitions[0].get("definition") if definitions else None
        #         )
        #         first_example = next(
        #             (
        #                 d.get("example").split(".")[0]
        #                 for d in definitions
        #                 if d.get("example")
        #             ),
        #             None,
        #         )
        #         meanings_by_pos[pos] = {
        #             "definition": first_definition,
        #             "example": first_example,
        #         }

        #     word_definitions.append(meanings_by_pos)
        meta = {"total": len(raw)}
        return UnifiedResponse(
            source="dictionary", provider="free", data=entries, meta=meta
        )
