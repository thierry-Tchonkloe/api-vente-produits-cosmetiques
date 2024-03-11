# routes/user.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from functions.admin import get_users, get_user, get_user_by_id, delete_user, password_forgot, password_forgot_verify
from schemas.user import UserCreate, LoginDataForm,  User as UserResponse, PasswordFormat
from schemas.admin import Admin as AdminResponse
from .auth import get_current_user, get_db, verify_password, create_access_token, get_current_admin



admin_router = APIRouter(prefix="/dashboard", tags=["Les actions sur les utilisateurs"], dependencies=[Depends(get_current_admin)])


@admin_router.get("/admin/", response_model=list[UserResponse], dependencies=[Depends(get_current_user)])
def read_users(db: Session = Depends(get_db)):
    return get_users(db)

@admin_router.get("/users/{user_id}", response_model=AdminResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="user not found",
        )
    return user
    

@admin_router.delete("/users/{user_id}", response_model=UserResponse)
def delete(user_id: int, db: Session = Depends(get_db)):
    return delete_user(db, user_id)