from sqlalchemy.orm import Session

from app.repositories.user_repository import UserRepository
from app.schemas.user import CreateUser
from app.core.security import hash_password, verify_password, create_access_token
from fastapi import HTTPException, status

class UserService:

    def __init__(self):
        self.user_repository = UserRepository()

    def create_user(self, db: Session, user_data: CreateUser):
        # Check if user already exists
        email = user_data.email.lower()

        existing_user = self.user_repository.get_user_by_email(db, email)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="User already exists"
            )

        hashed_password = hash_password(user_data.password)
        
        db_user = self.user_repository.create_user(
            db,
            email = email,
            hashed_password=hashed_password
        )

        return db_user
    

    def login_user(self, db: Session, email: str, password: str):
        email = email.lower()

        # Get user from DB
        user = self.user_repository.get_user_by_email(db, email)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=-"User not found"
            )
        
        # Verify password
        if not verify_password(password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials"
            )
        
        # Generate JWT token
        token = create_access_token(
            data={"sub": user.email}
        )

        return {"access_token": token, "token_type": "bearer"}