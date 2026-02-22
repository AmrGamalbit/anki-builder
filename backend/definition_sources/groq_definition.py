import json
import os

from dotenv import load_dotenv
from groq import Groq
from models import VocabularyResponse

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

client = Groq(
    api_key=os.getenv("API_KEY"),
)

def get_groq_definition(user_instructions):
    try:
        chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": SYSTEM_INSTRUCTIONS,
            },
            {
                "role": "user",
                "content": user_instructions,
            }
        ],
        model=MODEL,
        response_format={
                "type": "json_schema",
                "json_schema": {
                    "name": "Learning_Code",
                    "schema": VocabularyResponse.model_json_schema()
                }
        }
    )
        content = chat_completion.choices[0].message.content
        parsed = VocabularyResponse.model_validate_json(content)
        return parsed

    except:
        return "Something happened"
