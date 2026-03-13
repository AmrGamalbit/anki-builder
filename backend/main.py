from fastapi import FastAPI
from routes.ai import router as ai_router
from routes.dictionary import router as dictionary_router

app = FastAPI()
app.include_router(ai_router)
app.include_router(dictionary_router)


@app.get("/")
def index():
    return "server is running"
