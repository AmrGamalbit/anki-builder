# This is the deck generator for dictionaries.
# Simply provide data and a deck name to the constructor,
# and it will generate and store the deck. You can then call export_deck() to save it.
from services.base import BaseDeckGenerator


class DictionaryDeckGenerator(BaseDeckGenerator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.use_dictionary_audio = False

    def get_pronunciation_path(self, term: str):
        if self.use_dictionary_audio and self.pronunciation_url:
            path = self.pronunciation.fetch_pronunciation(
                term, self.pronunciation_url, self.temp_dir.name
            )
        else:
            path = self.pronunciation.generate_pronunciation(term, self.temp_dir.name)
        return path

    def build(self, data, deck_name: str = None):
        if deck_name != None:
            self.deck_name = deck_name
        notes = []
        for entry in data:
            for meaning in entry.meanings:
                for definition in meaning.definitions:
                    if self.use_dictionary_audio:
                        self.pronunciation_url = entry.pronunciation
                    example = definition.example if definition.example else ""
                    front = f"{entry.term}<br>({meaning.part_of_speech})"
                    back = f"{definition.text}<br>{example}"
                    note = self.create_note(
                        entry.term,
                        front,
                        back,
                    )
                    notes.append(note)
        self.deck = self.create_deck(notes, self.deck_name)
