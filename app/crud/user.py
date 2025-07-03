from app.models.user import User
from app.schemas.user import UserRegister
from sqlalchemy.orm import Session

def create_user(db: Session, user: UserRegister) -> User:
    model = User(**user.model_dump())
    db.add(model)
    db.commit()
    db.refresh(model)

    return model