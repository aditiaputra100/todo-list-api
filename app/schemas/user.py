from pydantic import BaseModel, Field

class UserRegister(BaseModel):
    name: str = Field(title="Name", description="Full name of the user", examples=["John Doe"])
    email: str = Field(title="Email", description="Email of the user", examples=["john_doe@email.com"])
    password: str = Field(title="Password", description="Password of the user", examples=["john123"])

class UserLogin(BaseModel):
    email: str = Field(title="Email", description="Email of the user", examples=["john_doe@email.com"])
    password: str = Field(title="Password", description="Password of the user", examples=["john123"])

class Token(BaseModel):
    access_token: str
    token_type: str

class User(BaseModel):
    id: int = Field(title="Id", description="Id of the user", examples=[1])
    email: str = Field(title="Email", description="Email of the user", examples=["john_doe@email.com"])
    name: str = Field(title="Name", description="Full name of the user", examples=["John Doe"])