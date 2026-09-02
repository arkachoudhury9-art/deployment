from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    name: str
    age: int = Field(ge=0)


class UserResponse(BaseModel):
    id: int
    name: str
    age: int

    model_config = {"from_attributes": True}
