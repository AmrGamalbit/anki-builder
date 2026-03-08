import json
import os

from dotenv import load_dotenv
from groq import Groq, APIConnectionError, RateLimitError, APIStatusError
from models.responses import AIResponseData, UnifiedResponse, AIResponse
from sources.base import BaseProvider

load_dotenv()

MODEL = "moonshotai/kimi-k2-instruct-0905"
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


class GroqProvider(BaseProvider):
    def __init__(self):
        self.client = Groq(
            api_key=os.getenv("API_KEY"),
        )

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
                model=MODEL,
                response_format={
                    "type": "json_schema",
                    "json_schema": {
                        "name": "Learning_Code",
                        "schema": AIResponse.model_json_schema(),
                    },
                },
            )
            return chat_completion.choices[0].message.content

        except RateLimitError:
            raise

        except APIConnectionError:
            raise

        except APIStatusError:
            raise

    def normalize(self, raw):
        definition_data = AIResponse.model_validate_json(raw)
        meta = {"model": MODEL}
        return UnifiedResponse(
            source="ai", provider="groq", data=definition_data.results, meta=meta
        )
