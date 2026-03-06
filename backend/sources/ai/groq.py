import json
import os

from dotenv import load_dotenv
from groq import Groq, APIConnectionError, RateLimitError, APIStatusError
from models.responses import AIResponseData, UnifiedResponse, AIResponse
from sources.base import BaseProvider

load_dotenv()

MODEL = "moonshotai/kimi-k2-instruct-0905"
SYSTEM_INSTRUCTIONS = """
# System Instructions

You are a highly intelligent linguistic expert with deep knowledge of all languages. You understand grammar, nuance, cultural context, and natural usage.

## Your Task

I will send you one or more words.
For each word, you must provide:

1. **A clear, accurate, and natural translation.**
2. **One simple example sentence** that demonstrates how the word is used in context.

## Guidelines

- The translation must be precise, natural, and easy to understand.
- Avoid overly technical, outdated, or unnatural wording.
- Do not provide multiple meanings unless they are essential.
- The example sentence must be clear, grammatically correct, and reflect real-life usage.
- Keep responses concise and well-structured.
- If a word has multiple common meanings, choose the most widely used one unless instructed otherwise.

Always prioritize clarity, correctness, and natural language usage.
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
