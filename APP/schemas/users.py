from pydantic import BaseModel


class CreateUserRequest(BaseModel):
    name: str
    email: str
    password: str
    c_password: str


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

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str
