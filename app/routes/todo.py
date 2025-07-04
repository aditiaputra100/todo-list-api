from typing import Annotated
from fastapi import APIRouter, Body, HTTPException, Depends
from starlette.status import HTTP_400_BAD_REQUEST
from app.schemas.todo import TodoCreate, TodoResponse
from app.schemas.user import User
from app.core.database import get_db
from app.crud import todo as todo_crud
from app.utils.auth import get_current_user
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/todo",
    tags=["Todo"]
)

@router.post("/", response_model=TodoResponse)
def create_todo(todo: Annotated[TodoCreate, Body()], user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    if todo.title == "":
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Title can't be null")

    if todo.description == "":
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Description can't be null")

    model = todo_crud.create_todo(db, todo, user.id)

    return model