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
from fastapi import BackgroundTasks
from app.tasks.background_tasks import send_email
from fastapi import Request
from app.core.limiter import limiter

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post(
    "/register",
    summary="Authenticate user",
    responses={
        200: {"description": "Login successful"},
        401: {"description": "Invalid credentials"},
        404: {"description": "User not found"},
        429: {"description": "Too many login attempts"}
    }
)
@limiter.limit("3/minute")
def register(
    request: Request,
    user: UserCreate,
    background_tasks: BackgroundTasks
):

    db = SessionLocal()

    result = register_user(
        db,
        user
    )

    db.close()

    # Execute after response is sent
    background_tasks.add_task(
        send_email,
        user.username
    )

    return result


@router.post(
    "/login",
    summary="Authenticate user",
    description="Validates username and password and returns a JWT access token."
)
@limiter.limit("5/minute")
def login(
    request: Request,
    user: UserCreate
):

    db = SessionLocal()

    result = login_user(
        db,
        user
    )

    db.close()

    return result