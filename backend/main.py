from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.ai import router as ai_router
from routes.dictionary import router as dictionary_router
from slowapi import Limiter
from slowapi.utils import get_remote_address
from slowapi.middleware import SlowAPIMiddleware
from utils.exceptions import register_handlers

app = FastAPI()
limiter = Limiter(key_func=get_remote_address, default_limits=["60/minute"])
app.state.limit = limiter
app.add_middleware(SlowAPIMiddleware)
app.include_router(ai_router)
app.include_router(dictionary_router)
register_handlers(app)

origins = ["http://localhost:5173"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def index():
    return "server is running"
