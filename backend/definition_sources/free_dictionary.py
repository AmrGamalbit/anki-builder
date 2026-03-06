import requests

def fetch_data(language_code: str, words: list):
    entries = []
    for index, word in enumerate(words): 
        url = f"https://api.dictionaryapi.dev/api/v2/entries/{language_code}/{word}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        first_word = data[0]
        phonetics = first_word.get("phonetics")[0]
        phonetics_pronunciation = phonetics.get("audio")
        phonetics_text = phonetics.get("text") or None
        meanings = first_word.get("meanings")[:3]
        first_definition = meanings[0].get("definitions")[0].get("definition")
        entries.append({
            "word": word,
            "meaning": first_definition,
            "pronunciation": phonetics_pronunciation,
            "phonetics_text": phonetics_text,
        })
    return entries