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


def build_anki_prompt(content, source_language, mode, options, target_language=None):
    """Call 2: generate Anki card data for the extracted terms"""
    return f"""You are given the following terms in {source_language}: {content}

    Your task is to {MODE_INSTRUCTIONS[mode].format(target_language=target_language)}.
    """
