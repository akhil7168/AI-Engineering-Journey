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

from app.core.logging_config import logger


def register_user(db, user):

    existing_user = (
        db.query(User)
        .filter(User.username == user.username)
        .first()
    )

    if existing_user:
        logger.warning(
            f"Registration failed. User already exists: {user.username}"
        )
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

    logger.info(
        f"User registered: {new_user.username}"
    )

    return {
        "message": "User registered"
    }


def login_user(db, user):

    db_user = (
        db.query(User)
        .filter(User.username == user.username)
        .first()
    )

    if not db_user:
        logger.warning(
            f"Login failed. User not found: {user.username}"
        )
        raise UserNotFoundException()

    if not verify_password(user.password, db_user.password):
        logger.warning(
            f"Invalid password for user: {user.username}"
        )
        raise InvalidCredentialsException()

    token = create_token(
        db_user.username
    )

    logger.info(
        f"User logged in: {db_user.username}"
    )

    return {
        "access_token": token
    }