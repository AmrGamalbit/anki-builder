from sources.base import BaseProvider
from google import genai
from google.genai.types import GenerateContentConfig
from models.responses import DefinitionsResponse, GenerateResponse
from dotenv import load_dotenv

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
- You must ALWAYS respond with a strict JSON array. One object per word.
- Return ONLY valid JSON. No preamble, no commentary, no markdown code blocks.
- Keep definitions and translations natural, concise, and accurate.
- Always use the most common meaning unless otherwise instructed.
- If a word is unknown or ambiguous, make your best reasonable attempt.
"""


class GeminiProvider(BaseProvider):
    def __init__(self, api_key: str, model: str | None = None):
        super().__init__(api_key, model)
        self.client = genai.Client(api_key=api_key)

    async def fetch(self, payload):
        response = self.client.models.generate_content(
            model=self.model,
            contents=payload.get("user_instructions"),
            config=GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTIONS,
                response_mime_type="application/json",
                response_json_schema=DefinitionsResponse.model_json_schema(),
            ),
        )
        return response.text

    def normalize(self, raw):
        data = DefinitionsResponse.model_validate_json(raw)
        meta = {"model": self.model}
        return GenerateResponse(
            source="ai", provider="gemini", data=data.results, meta=meta
        )

    def get_available_models(self):
        global _cached_models
        if _cached_models is None:
            _cached_models = [
                {"label": model.display_name, "value": model.name.split("/")[1]}
                for model in self.client.models.list()._page
                if "generateContent" in (model.supported_actions or [])
                and model.input_token_limit > 4096
                and not any(
                    word in model.name.lower()
                    for word in ["image", "video", "audio", "veo", "imagen"]
                )
            ]
        return _cached_models
