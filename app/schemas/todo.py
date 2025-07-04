from pydantic import BaseModel, Field

class TodoCreate(BaseModel):
    title: str = Field(title="Title", description="Title of todo", examples=["Example title"])
    description: str = Field(title="Description", description="Content of todo", examples=["This is a description of todo"])
    # user_id: int = Field(title="Id user", description="This identify of user", examples=[1])

class TodoResponse(BaseModel):
    id: int = Field(title="Id", description="Id of todo", examples=["6"])
    title: str = Field(title="Title", description="Title of todo", examples=["Example title"])
    description: str = Field(title="Description", description="Content of todo", examples=["This is a description of todo"])