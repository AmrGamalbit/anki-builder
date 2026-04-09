MODE_INSTRUCTIONS = {
    "definition": "provide a clear and simple definition for each term",
    "translation": "translate each term into {target_language}",
}


def build_user_instructions(
    content, source_language, mode, content_type, options, target_language=None
):
    if content_type == "terms":
        normalization = []
        if options.lowercase:
            normalization.append("convert to lowercase")
        if options.base_form:
            normalization.append(
                'use the base form of each word (e.g. "running" → "run")'
            )
        if options.strip_punctuation:
            normalization.append("strip any punctuation")

        normalization_instruction = (
            f"When processing each term: {', '.join(normalization)}."
            if normalization
            else ""
        )

        return f"""You are given the following terms in {source_language}: {content}

        Your task is to {MODE_INSTRUCTIONS[mode].format(target_language=target_language)}.

        {normalization_instruction}
        """
    else:
        idioms_instruction = (
            "Also extract idiomatic expressions."
            if options.include_idioms
            else "Focus on vocabulary only, no idioms."
        )

        return f"""
        You are given the following transcript in {source_language}:
        {content}

        Your task is to identify at most {options.max_cards} vocabulary terms and idioms 
        that a {options.vocabulary_level} learner would not know but should learn.
        {idioms_instruction}

        {MODE_INSTRUCTIONS[mode].format(target_language=target_language)}
        """
