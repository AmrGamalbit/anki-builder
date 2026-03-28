from gtts import gTTS
import os
import asyncio
import aiohttp


class PronunciationService:
    def __init__(self, lang):
        self.session = aiohttp.ClientSession()
        self.lang = lang

    def generate_pronunciation(self, term: str, media_folder: str) -> str:
        audio_path = os.path.join(media_folder, f"{term}.mp3")
        gTTS(text=term.split("<")[0], lang=self.lang, slow=False).save(audio_path)
        return {term: audio_path}

    async def fetch_pronunciation(
        self, term: str, pronunciation_url: str, media_folder: str
    ) -> str:
        audio_path = os.path.join(media_folder, f"{term}.mp3")
        async with self.session.get(pronunciation_url) as response:
            response.raise_for_status()
            content = await response.read()
            with open(audio_path, mode="wb") as file:
                file.write(content)
        return {term: audio_path}

    async def fetch_many(self, terms, pronunciation_urls, media_folder):
        results = await asyncio.gather(
            *[
                self.fetch_pronunciation(term, pronunciation_url, media_folder)
                for term, pronunciation_url in zip(terms, pronunciation_urls)
            ]
        )
        return {k: v for d in results for k, v in d.items() if v is not None}

    async def close_session(self):
        await self.session.close()
