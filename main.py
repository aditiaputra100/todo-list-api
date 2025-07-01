from fastapi import FastAPI
from app.routes import user
from app.database import SessionLocal

app = FastAPI()

app.include_router(user.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}