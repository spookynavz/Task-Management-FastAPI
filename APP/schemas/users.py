from pydantic import BaseModel
from typing import Optional, List

# Schema for User
class UserBase(BaseModel):
    name: str
    email: str


# Schema for Task
class TaskBase(BaseModel):
    title: str
    description: Optional[str]


