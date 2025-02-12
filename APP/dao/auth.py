from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.users import CreateUserRequest
from app.utils.auth import hash_password


def create_user(db: Session, user: CreateUserRequest):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = User(
        email=user.email,
        hashed_password = hash_password(user.password),
        name=user.name
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def get_user(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()
