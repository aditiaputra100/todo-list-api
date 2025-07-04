from typing import Annotated
from fastapi import APIRouter, Body, HTTPException, Depends
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_403_FORBIDDEN
from app.schemas.todo import Todo, TodoCreateResponse
from app.schemas.user import User
from app.core.database import get_db
from app.crud import todo as todo_crud
from app.utils.auth import get_current_user
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/todo",
    tags=["Todo"]
)

@router.post("/", response_model=TodoCreateResponse)
def create_todo(todo: Annotated[Todo, Body()], user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    if todo.title == "":
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Title can't be null")

    if todo.description == "":
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Description can't be null")

    model = todo_crud.create_todo(db, todo, user.id)

    return model

@router.put("/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, todo: Annotated[Todo, Body()], user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    model = todo_crud.get_todo_by_id(db, todo_id)

    if not model:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Todo not found")

    if model.user_id != user.id:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail=f"User id {user.id} doesn't have access to todo {model.id}")

    if todo.title == "":
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Title can't be null")

    if todo.description == "":
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Description can't be null")

    todo_crud.update_todo_by_id(db, todo_id, todo)

    return todo