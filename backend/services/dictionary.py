# This is the deck generator for dictionaries.
# Simply provide data and a deck name to the constructor,
# and it will generate and store the deck. You can then call export_deck() to save it.
from services.base import BaseDeckGenerator


class DictionaryDeckGenerator(BaseDeckGenerator):
    def __init__(self, use_dictionary_audio: bool = False, **kwargs):
        self.use_dictionary_audio = use_dictionary_audio
        super().__init__(**kwargs)

    async def get_pronunciations(self, terms: list[str], pronunciation_urls=None):
        pronunciations = {}
        if self.use_dictionary_audio:
            pronunciation_paths = await self.pronunciation_service.fetch_many(
                [term for term in terms if pronunciation_urls.get(term)],
                [
                    pronunciation_urls[key]
                    for key in terms
                    if pronunciation_urls.get(key)
                ],
                self.media_folder,
            )
            pronunciations.update(pronunciation_paths)
        else:
            for term in terms:
                pronunciation_path = self.pronunciation_service.generate_pronunciation(
                    term, self.media_folder
                )
                pronunciations.update(pronunciation_path)
        return pronunciations

    def parse_content(self, data):
        entries = []
        pronunciation_urls = {}
        for entry in data:
            for meaning in entry.meanings:
                for definition in meaning.definitions:
                    if self.use_dictionary_audio and not pronunciation_urls.get(
                        entry.term
                    ):
                        pronunciation_urls[entry.term] = entry.pronunciation
                    example = definition.example if definition.example else ""
                    front = f"{entry.term}<br>({meaning.part_of_speech})"
                    back = f"{definition.text}<br>{example}"
                    new_entry = (entry.term, front, back)
                    entries.append(new_entry)
        return entries, pronunciation_urls

    # async def build(self, data, deck_name: str = None):
    #     notes = []
    #     terms = [entry.term for entry in data]
    #     self.pronunciation_urls = {}
    #     if deck_name == None:
    #         self.deck_name = deck_name
    #     for entry in data:
    #         for meaning in entry.meanings:
    #             for definition in meaning.definitions:
    #                 if self.use_dictionary_audio and not self.pronunciation_urls.get(
    #                     entry.term
    #                 ):
    #                     self.pronunciation_urls[entry.term] = entry.pronunciation
    #                 example = definition.example if definition.example else ""
    #                 front = f"{entry.term}<br>({meaning.part_of_speech})"
    #                 back = f"{definition.text}<br>{example}"
    #                 note = self.create_note(
    #                     entry.term,
    #                     front,
    #                     back,
    #                 )
    #                 notes.append(note)
    #     self.deck = await self.create_deck(notes, terms, self.deck_name)
