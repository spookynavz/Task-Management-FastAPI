from typing import Annotated
from datetime import datetime, timedelta, timezone
from pydantic import BaseModel
from jose import JWTError, jwt
from starlette import status
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.schemas.users import CreateUserRequest, Token
from app.utils.auth import bcrypt_context, oauth2_bearer, create_access_token


router = APIRouter(prefix='/auth', tags=['auth'])

# Security settings
SECRET_KEY = "83498230ejdifvnda"
ALGORITHM = "HS256" 

# # Password hashing
# bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# oauth2_bearer = OAuth2PasswordBearer(tokenUrl="/users/login/")

# class CreateUserRequest(BaseModel):
#     username: str
#     password: str

# class Token(BaseModel):
#     access_token: str
#     token_type: str


db_dependency = Annotated[Session, Depends(get_db)]


@router.post("/", status_code= status.HTTP_201_CREATED)
async def create_user(db:db_dependency, create_user_request:CreateUserRequest):
    create_user_model = User(username = create_user_request.username, hashed_password = bcrypt_context.hash(create_user_request.password))
    db.add()
    db.commit()


@router.post("/token", response_model = Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = authenticate_user(form_data.username, form_data.password, db)

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail = "couldnt validate user")
    
    token = create_access_token(user.username, user.id, timedelta(minutes=20))

    return {"access_token":token, "token_type":"bearer"}



def authenticate_user(username:str, password:str, db):
    user = db.query(User).filter(User.username==username).first()
    if not user:
        return False    
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return user


# # Token functions
# def create_access_token(username:str, user_id:int, expires_delta: timedelta):
#     to_encode = {"sub": username, "id":user_id}
#     expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=20))
#     to_encode.update({"exp": expire})
#     return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)