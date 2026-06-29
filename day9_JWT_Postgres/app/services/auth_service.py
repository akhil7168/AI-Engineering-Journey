from fastapi import HTTPException

from models import User
from auth import (
    hash_password,
    verify_password
)
from jwt_handler import create_token

from app.exceptions.custom_exceptions import (
    UserAlreadyExistsException,
    UserNotFoundException,
    InvalidCredentialsException
)

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

        raise UserAlreadyExistsException()
    
    hashed_password = hash_password(user.password)

    new_user = User(
    username=user.username,
    password=hashed_password,
    role="user"
)

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return {
        "message": "User registered"
    }

def login_user(db, user):

    print("=" * 60)
    print("INPUT USERNAME:", repr(user.username))

    users = db.query(User).all()
    print("ALL USERS:", [(u.id, u.username) for u in users])

    db_user = (
        db.query(User)
        .filter(User.username == user.username)
        .first()
    )

    print("MATCHED USER:", db_user)

    if not db_user:
        raise UserNotFoundException()

    if not verify_password(
        user.password,
        db_user.password
    ):
        raise InvalidCredentialsException()

    token = create_token(user.username)

    return {
        "access_token": token
    }