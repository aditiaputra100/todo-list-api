from pydantic import BaseModel, Field

class UserRegister(BaseModel):
    name: str = Field(title="Name", description="Full name of the user", examples=["John Doe"])
    email: str = Field(title="Email", description="Email of the user", examples=["john_doe@email.com"])
    password: str = Field(title="Password", description="Password of the user", examples=["john123"])


class Token(BaseModel):
    access_token: str
    token_type: str