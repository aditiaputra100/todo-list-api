from fastapi import FastAPI
from app.routes import user
from app.core.config import Settings

app = FastAPI(title=Settings.APP_NAME)

app.include_router(user.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}