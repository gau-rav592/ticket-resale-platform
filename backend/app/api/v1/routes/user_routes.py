from fastapi import APIRouter, Depends, Form
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.user import CreateUser, UserOut
from app.services.user_service import UserService
from app.api.deps import get_current_user

router = APIRouter()


@router.post("/signup", response_model=UserOut)
def signup(user_data: CreateUser, db: Session = Depends(get_db)):
    user_service = UserService()
    user = user_service.create_user(db, user_data)
    return user

@router.post("/login")
def login(email: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    user_service = UserService()
    return user_service.login_user(db, email, password)

@router.get("/me", response_model=UserOut)
def get_me(current_user = Depends(get_current_user)):
    return current_user