from fastapi import FastAPI
from app.routes import user
from app.core.config import Settings
from dotenv import load_dotenv
from pathlib import Path
import os

dev_mode = True if "dev" in os.getenv("ENVIRONMENT", "dev") == "dev" else False
env_path = Path(__file__).resolve().parent / ".env.development" if dev_mode else Path(__file__).resolve().parent / ".env.production"

load_dotenv(dotenv_path=env_path)

app = FastAPI(title=Settings.APP_NAME)

app.include_router(user.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}