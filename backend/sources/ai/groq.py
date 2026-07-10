from dotenv import load_dotenv
from groq import Groq
from models.responses import DefinitionsResponse, GenerateResponse
from sources.base import BaseProvider

load_dotenv()

_cached_models = None
SYSTEM_INSTRUCTIONS = """
You are an expert linguist with deep knowledge of languages, grammar, cultural context, and natural usage.

## Modes

The user will specify a mode for each request. You must strictly follow the behavior defined for that mode:

### MODE: translation
- Translate the given word(s) into the specified target language.
- Provide the most common, natural translation.
- Include one short, real-life example sentence in the **target language**.

### MODE: definition
- Define the given word(s) in clear, plain English.
- Focus on the most widely used meaning unless context suggests otherwise.
- Include one short, real-life example sentence in **English**.

## Rules
You must respond with a JSON object matching this exact structure:
{
  "results": [
    {
      "term": "the original word",
      "definition": "clear definition or translation",
      "synonyms": ["synonym1", "synonym2"] or null,
      "antonyms": ["antonym1"] or null,
      "example": "one example sentence" or null,
      "part_of_speech": "noun/verb/adjective/adverb/etc",
      "audio_url": null,
      "pictogram_url": null
    }
  ]
}

- Return ONLY valid JSON. No preamble, no commentary, no markdown code blocks.
- `audio_url` and `pictogram_url` must always be null — do not generate URLs.
- `synonyms` and `antonyms` should be null if none are relevant.
- Every object in results must have all fields listed above.
- Never return a raw array, always wrap in a results key.
"""


class GroqProvider(BaseProvider):
    def __init__(self, api_key: str, model: str | None = None):
        self.client = Groq(
            api_key=api_key,
        )
        self.model = model

    async def fetch(self, payload):
        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": SYSTEM_INSTRUCTIONS,
                    },
                    {
                        "role": "user",
                        "content": payload.get("user_instructions"),
                    },
                ],
                model=self.model,
                response_format={
                    "type": "json_schema",
                    "json_schema": {
                        "name": "Learning_Vocab",
                        "schema": DefinitionsResponse.model_json_schema(),
                    },
                },
            )
            return chat_completion.choices[0].message.content

        except Exception as e:
            try:
                chat_completion = self.client.chat.completions.create(
                    messages=[
                        {
                            "role": "system",
                            "content": SYSTEM_INSTRUCTIONS,
                        },
                        {
                            "role": "user",
                            "content": payload.get("user_instructions"),
                        },
                    ],
                    model=self.model,
                )
                return chat_completion.choices[0].message.content
            except Exception as e:
                print(f"First attempt failed: {e}")

    def normalize(self, raw):
        start = raw.index("{")
        end = raw.rindex("}")
        raw = raw[start : end + 1]
        data = DefinitionsResponse.model_validate_json(raw)
        meta = {"model": self.model}
        return GenerateResponse(
            source="ai", provider="groq", data=data.results, meta=meta
        )

    def get_available_models(self):
        global _cached_models
        if _cached_models is None:
            _cached_models = [
                {"label": model.id, "value": model.id}
                for model in self.client.models.list().data
                if "text" in model.input_modalities
                and "text" in model.output_modalities
                and model.context_window > 4096
                and "json_mode" in (model.supported_features or [])
            ]
        return _cached_models
