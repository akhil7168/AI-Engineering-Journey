from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session

from models import User
from schemas import UserCreate
from database import SessionLocal
from auth import hash_password, verify_password
from jwt_handler import create_token
from app.services.auth_service import (
    register_user,
    login_user
)


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/register")
def register(user: UserCreate):

    db = SessionLocal()

    result = register_user(
        db,
        user
    )

    db.close()

    return result


@router.post("/login")
def login(user: UserCreate):

    db = SessionLocal()

    result = login_user(
        db,
        user
    )

    db.close()

    return result