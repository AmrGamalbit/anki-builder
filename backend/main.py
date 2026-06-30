from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from routes.ai import router as ai_router
from routes.dictionary import router as dictionary_router
from routes.file import router as file_router
from routes.styles import router as styles_router
from routes.export import router as export_router
from routes.auth import router as auth_router
from slowapi import Limiter
from slowapi.middleware import SlowAPIMiddleware
from slowapi.util import get_remote_address
from utils.exceptions import register_handlers
from dotenv import load_dotenv
import os


load_dotenv()
app = FastAPI()
limiter = Limiter(key_func=get_remote_address, default_limits=["60/minute"])
app.state.limiter = limiter

origins = ["http://localhost:5173", "http://127.0.0.1:5173"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(SlowAPIMiddleware)
app.add_middleware(
    SessionMiddleware,
    secret_key=os.getenv("SESSION_SECRET_KEY"),
    same_site="none",
    https_only=True,
)

app.include_router(ai_router)
app.include_router(dictionary_router)
app.include_router(file_router)
app.include_router(styles_router)
app.include_router(export_router)
app.include_router(auth_router)
register_handlers(app)


@app.get("/")
def index():
    return "server is running"
