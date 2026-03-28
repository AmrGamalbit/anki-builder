# This is the deck generator for AI models.
# Simply provide data and a deck name to the constructor,
# and it will generate and store the deck. You can then call export_deck() to save it.
from services.base import BaseDeckGenerator


class AIDeckGenerator(BaseDeckGenerator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def parse_content(self, data):
        entries = []
        for entry in data:
            entries.append(
                (entry.term, f"{entry.term}<br><br>{entry.example}", entry.result)
            )
        return entries, None

    async def get_pronunciations(self, terms: list[str], pronunciation_urls=None):
        pronunciations = {}
        for term in terms:
            pronunciation_path = self.pronunciation_service.generate_pronunciation(
                term, self.temp_dir.name
            )
            pronunciations.update(pronunciation_path)
        return pronunciations
