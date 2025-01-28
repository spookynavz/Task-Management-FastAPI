from pydantic import BaseModel
from typing import Optional, List

# Schema for User
class UserBase(BaseModel):
    name: str
    email: str


