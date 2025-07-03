from fastapi.params import Depends

from app.schemas.user import UserRegister, Token
from app.core.config import Settings
from app.core.database import get_db
from app.crud.user import create_user
from datetime import timedelta, datetime, timezone
from email_validator import validate_email, EmailNotValidError
from fastapi import APIRouter, Body, HTTPException
from passlib.context import CryptContext
from starlette.status import HTTP_400_BAD_REQUEST
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import Annotated
import jwt

router = APIRouter()

JWT_SECRET_KEY = Settings.JWT_SECRET_KEY
JWT_ALGORITHM = Settings.JWT_ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = Settings.ACCESS_TOKEN_EXPIRE_MINUTES

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def create_access_token(data: dict[str, any], expired_token: timedelta):
    to_encode = data.copy()

    expired = datetime.now(timezone.utc) + expired_token

    to_encode.update({"exp": expired})

    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, JWT_ALGORITHM)

    return encoded_jwt

@router.post("/register")
def register(user: Annotated[UserRegister, Body()], db: Session = Depends(get_db)):
    try:
        email = validate_email(user.email, check_deliverability=True)

        email = email.normalized
    except EmailNotValidError as e:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=str(e))

    password: str = user.password

    if len(password) < 8:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Password length must be more than 8 characters!")

    name: str = user.name

    if not name:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Name must be filled!")

    password = hash_password(password)

    expired_token = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    user.password = password

    try:
        user_model = create_user(db, user)
    except IntegrityError as err:
        db.rollback()

        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Email already registered!")
    finally:
        db.close()

    access_token = create_access_token(
        data={
            "id": user_model.id,
            "email": email,
            "name": name
        },
        expired_token=expired_token
    )

    return Token(access_token=access_token, token_type="bearer")