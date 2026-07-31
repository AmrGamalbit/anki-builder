import spacy
from cefrpy import CEFRSpaCyAnalyzer, CEFRLevel

ABBREVIATION_MAPPING = {
    "'m": "am",
    "'s": "is",
    "'re": "are",
    "'ve": "have",
    "'d": "had",
    "n't": "not",
    "'ll": "will",
}

ENTITY_TYPES_TO_SKIP_CEFR = {
    "PERSON",
    "ORG",
    "GPE",
    "LOC",
    "FAC",
    "PRODUCT",
    "WORK_OF_ART",
    "LAW",
    "MONEY",
    "QUANTITY",
}
nlp = spacy.load("en_core_web_sm")
text_analyzer = CEFRSpaCyAnalyzer(
    entity_types_to_skip=ENTITY_TYPES_TO_SKIP_CEFR,
    abbreviation_mapping=ABBREVIATION_MAPPING,
)


def analyze_text(text: str) -> dict:
    doc = nlp(text)
    tokens = text_analyzer.analyze_doc(doc)
    result = {}
    for token in tokens:
        word, score = token[0], token[3]
        if score:
            result[word] = CEFRLevel(round(score)).name
    return result