from gtts import gTTS
import os
import requests


class PronunciationService:
    def __init__(self, lang):
        self.lang = lang

    def generate_pronunciation(self, term: str, media_folder: str) -> str:
        audio_path = os.path.join(media_folder, f"{term}.mp3")
        gTTS(text=term.split("<")[0], lang=self.lang, slow=False).save(audio_path)
        return audio_path

    def fetch_pronunciation(
        self, term: str, pronunciation_url: str, media_folder: str
    ) -> str:
        print(pronunciation_url)
        audio_path = os.path.join(media_folder, f"{term}.mp3")
        response = requests.get(
            pronunciation_url, headers={"User-Agent": "Mozilla/5.0"}
        )
        response.raise_for_status()
        with open(audio_path, mode="wb") as file:
            file.write(response.content)
        return audio_path
