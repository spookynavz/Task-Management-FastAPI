from fastapi import Depends, HTTPException, status
from app.models.user import User
from app.utils.auth import get_current_user


def auth_required(current_user: User = Depends(get_current_user)):
    if current_user.role not in ["Employee", "Admin"]:
        raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED, detail="Authentication required")
    return current_user


def manager_required(current_user: User = Depends(get_current_user)):
    if current_user.role not in ["Manager", "Admin"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only Managers are allowed")
    return current_user


def admin_required(current_user: User = Depends(get_current_user)):
    if current_user.role != "Admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only Admins are allowed")
    return current_user
