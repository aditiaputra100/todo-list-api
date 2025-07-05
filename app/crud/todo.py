from app.models.todo import Todo
from app.schemas.todo import Todo as TodoSchema
from sqlalchemy.orm import Session

def create_todo(db: Session, todo: TodoSchema, user_id: int) -> Todo:
    model = Todo(**todo.model_dump(), user_id=user_id)

    db.add(model)
    db.commit()
    db.refresh(model)

    return model

def get_todo_by_id(db: Session, todo_id: int) -> Todo | None:
    todo = db.query(Todo).where(Todo.id == todo_id).first()

    return todo

def update_todo_by_id(db: Session, todo_id: int, todo: TodoSchema):
    db.query(Todo).where(Todo.id == todo_id).update(todo.model_dump())

    db.commit()

def delete_todo_by_id(db: Session, todo_id: int) -> None:
    db.query(Todo).where(Todo.id == todo_id).delete()

    db.commit()