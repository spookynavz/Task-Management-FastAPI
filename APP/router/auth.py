from fastapi import Depends, HTTPException, APIRouter, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.dao.auth import create_user, get_user
from app.utils.auth import create_access_token, verify_password
from app.schemas.users import (
    CreateUserRequest, UserLoginRequest,
    UserRegisterResponse, UserLoginResponse
)

router = APIRouter(prefix='/user', tags=['user'])
 

@router.post("/register", response_model=UserRegisterResponse)
def register(user: CreateUserRequest, db: Session = Depends(get_db)):
    if user.password != user.c_password:
        raise HTTPException(
            status_code=400,
            detail="Password and Confirm Password do not match"
        )
    return create_user(db, user)



@router.post("/login", response_model=UserLoginResponse)
def login(body: UserLoginRequest, db: Session = Depends(get_db)):
    db_user = get_user(db, body.email)

    if db_user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    # Verify password
    if not verify_password(body.password, db_user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    # Create JWT token
    access_token = create_access_token(email=db_user.email, user_id=db_user.id)

    # Return the token in the response
    return {"access_token": access_token, "token_type": "bearer"}
