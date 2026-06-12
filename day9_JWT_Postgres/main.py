from fastapi import FastAPI
from fastapi import HTTPException
from jwt_handler import create_token
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi import Header
from jwt_handler import verify_token

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

    print("Step 1")

    db: Session = SessionLocal()

    print("Step 2")

    db_user = (
        db.query(User)
        .filter(User.username == user.username)
        .first()
    )

    print("Step 3")

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    print("Step 4")

    result = verify_password(
        user.password,
        db_user.password
    )

    print("Password Verify Result:", result)

    print("Step 5")

    token = create_token(user.username)

    print("Generated Token:", token)

    print("Step 6")

    db.close()

    return {
        "access_token": token
    }

    return {
        "access_token": token
    }
def get_current_user(
    authorization: str = Header(None)
):

    if authorization is None:

        raise HTTPException(
            status_code=401,
            detail="Token Missing"
        )

    token = authorization.replace(
        "Bearer ",
        ""
    )

    payload = verify_token(token)

    if payload is None:

        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )

    return payload

@app.get("/profile")
def profile(
    user=Depends(get_current_user)
):

    return {
        "message": "Protected Route Accessed",
        "user": user
    }

@app.get("/me")
def get_me(
    user=Depends(get_current_user)
):
    return user