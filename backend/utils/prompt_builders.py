MODE_INSTRUCTIONS = {
    "definition": "provide a clear and simple definition for each term",
    "translation": "translate each term into {target_language}",
}


def build_extraction_prompt(content, source_language, provider, options):
    """Call 1: extract unusual words/idioms from transcript"""
    idioms_instruction = (
        "Also extract idiomatic expressions."
        if options.include_idioms and provider != "free_dictionary_api"
        else "Focus on vocabulary only, no idioms."
    )
    return f"""
    You are given the following transcript in {source_language}:
    {content}

    Identify at most {options.max_cards} vocabulary terms and idioms 
    that a {options.vocabulary_level} learner would not know but should learn.
    {idioms_instruction}

    Return only a JSON list of terms, nothing else.
    """


def build_user_instructions(terms, definition_options):
    terms_str = ", ".join(terms)
    mode_instruction = MODE_INSTRUCTIONS[definition_options.mode].format(
        source_language=definition_options.source_language,
        target_language=definition_options.target_language,
    )

    fields = definition_options.card_fields
    requested_fields = []
    if fields.part_of_speech:
        requested_fields.append("part of speech")
    if fields.example:
        requested_fields.append("an example sentence")
    if fields.synonyms:
        requested_fields.append("synonyms")
    if fields.antonyms:
        requested_fields.append("antonyms")

    fields_instruction = (
        f"Include: {', '.join(requested_fields)}. Do not include any other fields."
    )
    return f"""Generate Anki flashcard data for the following {definition_options.source_language} terms: {terms_str}

Task: {mode_instruction}

{fields_instruction}

Return one object per term. Do not skip any terms. If a term is unknown or ambiguous, make your best attempt."""
