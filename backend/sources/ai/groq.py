import os

from dotenv import load_dotenv
from groq import Groq
from models.responses import UnifiedResponse, AIResponse
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
      "term": "the word",
      "result": "definition or translation",
      "example": "example sentence"
    }
  ]
}

- Return ONLY valid JSON. No preamble, no commentary, no markdown code blocks.
- Every object in results must have exactly these three fields: term, result, example.
- Never return a raw array, always wrap in a results key.
"""


class GroqProvider(BaseProvider):
    def __init__(self, api_key: str):
        self.client = Groq(
            api_key=api_key,
        )

    async def fetch(self, payload, model):
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
                model=model,
                response_format={
                    "type": "json_schema",
                    "json_schema": {
                        "name": "Learning_Vocab",
                        "schema": AIResponse.model_json_schema(),
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
                    model=model,
                )
                return chat_completion.choices[0].message.content
            except Exception as e:
                print(f"First attempt failed: {e}")

    def normalize(self, raw, model):
        start = raw.index("{")
        end = raw.rindex("}")
        raw = raw[start : end + 1]
        definition_data = AIResponse.model_validate_json(raw)
        meta = {"model": model}
        return UnifiedResponse(
            source="ai", provider="groq", data=definition_data.results, meta=meta
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
