from pydantic import BaseModel, Field, ConfigDict
from app.models.todo import Todo
from typing import List, Type

class Todo(BaseModel):
    title: str = Field(title="Title", description="Title of todo", examples=["Example title"])
    description: str = Field(title="Description", description="Content of todo", examples=["This is a description of todo"])
    # user_id: int = Field(title="Id user", description="This identify of user", examples=[1])

class TodoCreateResponse(BaseModel):
    id: int = Field(title="Id", description="Id of todo", examples=["6"])
    title: str = Field(title="Title", description="Title of todo", examples=["Example title"])
    description: str = Field(title="Description", description="Content of todo", examples=["This is a description of todo"])

class TodoResponse(BaseModel):
    title: str = Field(title="Title", description="Title of todo", examples=["Example title"])
    description: str = Field(title="Description", description="Content of todo",
                             examples=["This is a description of todo"])
    id: int = Field(title="Id user", description="This identify of user", examples=[1])

    model_config = ConfigDict(from_attributes=True)

class TodoListResponse(BaseModel):
    data: List[TodoResponse] = Field(title="Data", description="List of todo", examples=[[TodoResponse(id=1, title="Example title", description="Example description")]])
    page: int = Field(title="Page", description="Pages retrieved from database", gt=0, examples=[1, 2, 9])
    limit: int = Field(title="Limit", description="Limit of data taken", gt=0, examples=[10, 15, 20])
    total: int = Field(title="Total", description="Total number of todos", examples=[1, 4, 7])
