from fastapi import FastAPI
from app.routes import user, todo
from app.core.config import Settings

app = FastAPI(title=Settings.APP_NAME)

app.include_router(user.router)
app.include_router(todo.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}