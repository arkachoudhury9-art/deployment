from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.models import User
from backend.schemas import UserCreate, UserResponse

router = APIRouter()
DbSession = Annotated[Session, Depends(get_db)]


@router.get("/users", response_model=list[UserResponse])
def get_users(db: DbSession):
    return db.scalars(select(User)).all()


@router.post("/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: DbSession):
    db_user = User(name=user.name, age=user.age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
