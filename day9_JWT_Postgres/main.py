from fastapi import FastAPI
from fastapi import HTTPException
from jwt_handler import create_token
from sqlalchemy.orm import Session

from database import (
    SessionLocal,
    engine,
    Base
)

from models import User

from schemas import UserCreate

from auth import (
    hash_password,
    verify_password
)

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.post("/register")
def register(user: UserCreate):

    db: Session = SessionLocal()

    existing_user = (
        db.query(User)
        .filter(
            User.username == user.username
        )
        .first()
    )

    if existing_user:

        raise HTTPException(
            status_code=400,
            detail="User already exists"
        )

    new_user = User(
        username=user.username,
        password=hash_password(
            user.password
        )
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    db.close()

    return {
        "message": "User registered"
    }
@app.post("/login")
def login(user: UserCreate):

    db: Session = SessionLocal()

    db_user = (
        db.query(User)
        .filter(User.username == user.username)
        .first()
    )

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    if not verify_password(
        user.password,
        db_user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Wrong password"
        )

    token = create_token(user.username)

    db.close()

    return {
        "access_token": token
    }