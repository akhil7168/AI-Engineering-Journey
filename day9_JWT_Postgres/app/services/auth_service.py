from fastapi import HTTPException

from models import User
from auth import (
    hash_password,
    verify_password
)
from jwt_handler import create_token

def register_user(
    db,
    user
):

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

    return {
        "message": "User registered"
    }

def login_user(
    db,
    user
):

    db_user = (
        db.query(User)
        .filter(
            User.username == user.username
        )
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

    token = create_token(
        user.username
    )

    return {
        "access_token": token
    }