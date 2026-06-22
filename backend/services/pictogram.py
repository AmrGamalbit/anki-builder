import os
import asyncio
import aiohttp


class PictogramService:
    def __init__(self, media_folder):
        self.BASE_URL = "https://api.arasaac.org/api/pictograms/en/search/{term}"
        self.session = aiohttp.ClientSession()
        self.media_folder = media_folder

    async def get_url(self, term: str) -> str:
        term_url = self.BASE_URL.format(term=term)
        try:
            async with self.session.get(term_url) as response:
                response.raise_for_status()
                results = await response.json()
                pictogram_id = results[0].get("_id")
                pictogram_url = f"https://static.arasaac.org/pictograms/{pictogram_id}/{pictogram_id}_300.png"
                return pictogram_url

        except aiohttp.ClientError as e:
            print(f"Error fetching data from {term_url}: {e}")
            return None

        except asyncio.TimeoutError:
            print(f"Request to {term} timed out")
            return None

    async def fetch(self, pictogram_url: str, term: str) -> dict:
        pictogram_path = os.path.join(self.media_folder, f"{term}.png")
        if not pictogram_url:
            return {term: None}

        try:
            async with self.session.get(pictogram_url) as response:
                response.raise_for_status()
                content = await response.read()
                with open(pictogram_path, mode="wb") as file:
                    file.write(content)
                return {term: pictogram_path}

        except aiohttp.ClientError as e:
            print(f"Error fetching data from {pictogram_url}: {e}")
            return {term: None}

        except asyncio.TimeoutError:
            print(f"Request to {term} timed out")
            return {term: None}

    async def fetch_many(self, terms: [str]) -> dict:
        urls = await asyncio.gather(*[self.get_url(term) for term in terms])
        results = await asyncio.gather(
            *[self.fetch(url, term) for term, url in zip(terms, urls)]
        )
        return {k: v for d in results for k, v in d.items() if v is not None}

    async def close_session(self):
        await self.session.close()
