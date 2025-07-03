from app.models.user import User
from app.schemas.user import UserRegister, UserLogin
from sqlalchemy.orm import Session

def create_user(db: Session, user: UserRegister) -> User:
    model = User(**user.model_dump())
    db.add(model)
    db.commit()
    db.refresh(model)

    return model

def get_user_by_email(db: Session, email: str) -> User | None:
    user_model = db.query(User).where(User.email == email).first()

    if not user_model:
        return None

    print(user_model.email)
    print(user_model.password)

    return user_model
