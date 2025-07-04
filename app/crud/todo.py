from app.models.todo import Todo
from app.schemas.todo import TodoCreate
from sqlalchemy.orm import Session

def create_todo(db: Session, todo: TodoCreate, user_id: int) -> Todo:
    model = Todo(**todo.model_dump(), user_id=user_id)

    db.add(model)
    db.commit()
    db.refresh(model)

    return model