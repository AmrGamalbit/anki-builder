from fastapi import FastAPI
from fastapi.responses import JSONResponse
from google.genai import errors
from groq import APIConnectionError, RateLimitError, APIStatusError
from gtts.tts import gTTSError


def register_handlers(app: FastAPI):
    @app.exception_handler(Exception)
    def generic_handler(request, exc):
        return JSONResponse(status_code=500, content={"detail": str(exc)})

    @app.exception_handler(errors.APIError)
    def google_handler(request, exc):
        return JSONResponse(status_code=exc.code, content={"detail": exc.message})

    @app.exception_handler(APIConnectionError)
    def groq_connection_handler(request, exc):
        return JSONResponse(
            status_code=502, content={"detail": "Could not reach AI service"}
        )

    @app.exception_handler(RateLimitError)
    def groq_ratelimit_handler(request, exc):
        return JSONResponse(status_code=429, content={"detail": "AI quota exceeded"})

    @app.exception_handler(APIStatusError)
    def groq_status_handler(request, exc):
        return JSONResponse(status_code=exc.status_code, content={"detail": str(exc)})

    @app.exception_handler(gTTSError)
    def gtts_handler(request, exc):
        return JSONResponse(status_code=502, content={"detail": str(exc)})
