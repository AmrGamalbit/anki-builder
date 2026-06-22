from models.responses import CardData


def normalize_dictionary_entries(entries: list, use_dictionary_audio: bool):
    cards = []
    pronunciation_urls = {}
    for entry in entries:
        for meaning in entry.meanings:
            for definition in meaning.definitions:
                if use_dictionary_audio and not pronunciation_urls.get(entry.term):
                    pronunciation_urls[entry.term] = entry.pronunciation
                example = definition.example if definition.example else ""
                front = f"{entry.term}\n({meaning.part_of_speech})"
                back = f"{definition.text}\n{example}"
                cards.append(CardData(term=entry.term, front=front, back=back))
    return cards, pronunciation_urls
