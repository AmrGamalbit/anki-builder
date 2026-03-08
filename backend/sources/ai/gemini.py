from sources.base import BaseProvider
from google import genai
from google.genai.types import GenerateContentConfig
from models.responses import AIResponseData, UnifiedResponse, AIResponse
import os
from dotenv import load_dotenv

load_dotenv()

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

MODEL = "gemini-2.5-flash"


class GeminiProvider(BaseProvider):
    def __init__(self):
        self.client = genai.Client(api_key=os.getenv("api"))

    async def fetch(self, payload):
        response = self.client.models.generate_content(
            model=MODEL,
            contents=payload.get("user_instructions"),
            config=GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTIONS,
                response_mime_type="application/json",
                response_json_schema=AIResponse.model_json_schema(),
            ),
        )
        return response.text

    def normalize(self, raw):
        definition_data = AIResponse.model_validate_json(raw)
        meta = {"model": MODEL}
        return UnifiedResponse(
            source="ai", provider="gemini", data=definition_data.results, meta=meta
        )
