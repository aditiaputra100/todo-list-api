from app.schemas.user import UserRegister
from email_validator import validate_email, EmailNotValidError
from fastapi import APIRouter, Body, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST
from typing import Annotated

router = APIRouter()

@router.post("/register")
def register(user: Annotated[UserRegister, Body()]):
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

    return {
        "name": name,
        "email": email,
        "password": password
    }