import os
import requests


class PictogramService:
    def __init__(self):
        self.BASE_URL = "https://api.arasaac.org/api/pictograms/en/search/{term}"

    def get_url(self, term: str) -> str:
        self.term = term
        print(self.term)
        try:
            response = requests.get(
                self.BASE_URL.format(term=term),
                headers={"User-Agent": "Mozilla/5.0"},
            )
            response.raise_for_status()
            results = response.json()
            pictogram_id = results[0].get("_id")
            return f"https://static.arasaac.org/pictograms/{pictogram_id}/{pictogram_id}_300.png"

        except requests.exceptions.HTTPError as errh:
            print("HTTP Error")
            print(errh.args[0])
            return None

    def fetch_pictogram(self, pictogram_url: str, media_folder) -> list[str]:
        pictogram_path = os.path.join(media_folder, f"{self.term}.png")
        if not pictogram_url:
            return None

        try:
            response = requests.get(
                pictogram_url, headers={"User-Agent": "Mozilla/5.0"}
            )
            response.raise_for_status()
            with open(pictogram_path, mode="wb") as file:
                file.write(response.content)
            return pictogram_path

        except requests.exceptions.HTTPError as errh:
            print("HTTP Error")
            print(errh.args[0])
            return None
