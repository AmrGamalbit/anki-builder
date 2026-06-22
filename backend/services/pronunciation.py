from gtts import gTTS
import os
import asyncio
import aiohttp


class PronunciationService:
    def __init__(self, lang: str, media_folder: str):
        self.session = aiohttp.ClientSession()
        self.lang = lang
        self.media_folder = media_folder

    def generate(self, term: str) -> dict:
        audio_path = os.path.join(self.media_folder, f"{term}.mp3")
        gTTS(text=term.split("<")[0], lang=self.lang, slow=False).save(audio_path)
        return {term: audio_path}

    def generate_many(self, terms: list[str]) -> dict:
        results = {}
        for term in terms:
            results.update(self.generate(term))
        return results

    async def fetch(
        self,
        term: str,
        pronunciation_url: str,
    ) -> dict:
        audio_path = os.path.join(self.media_folder, f"{term}.mp3")
        async with self.session.get(pronunciation_url) as response:
            response.raise_for_status()
            content = await response.read()
            with open(audio_path, mode="wb") as file:
                file.write(content)
        return {term: audio_path}

    async def fetch_many(
        self, terms: list[str], pronunciation_urls: dict[str, str]
    ) -> dict:
        results = await asyncio.gather(
            *[self.fetch(term, pronunciation_urls.get(term)) for term in terms]
        )
        return {k: v for d in results for k, v in d.items() if v is not None}

    async def close_session(self):
        await self.session.close()
