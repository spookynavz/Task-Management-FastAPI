from pydantic import BaseModel
from typing import Optional, List

# Schema for User
class UserBase(BaseModel):
    name: str
    email: str


class CreateUserRequest(BaseModel):
    name: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

