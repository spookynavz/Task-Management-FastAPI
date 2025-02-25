from pydantic import BaseModel
import enum
from sqlalchemy import Enum
from typing import Optional

class RoleEnum(str, enum.Enum): 
    ADMIN = "Admin"
    MANAGER = "Manager"
    EMPLOYEE = "Employee"


class CreateUserRequest(BaseModel):
    name: str
    email: str
    password: str
    c_password: str
    role: Optional[RoleEnum] = RoleEnum.EMPLOYEE


class UserLoginRequest(BaseModel):
    email: str
    password: str


class UserLoginResponse(BaseModel):
    access_token: str
    token_type: str


class UserRegisterResponse(BaseModel):
    id: int
    name: str
    email: str
    role: RoleEnum

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str