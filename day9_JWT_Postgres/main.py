from fastapi import FastAPI

from database import Base, engine

from app.routers.auth_routes import router as auth_router
from app.routers.note_routes import router as note_router

from app.exceptions.handlers import (
    user_exists_handler,
    user_not_found_handler,
    invalid_credentials_handler,
    invalid_token_handler,
    note_not_found_handler
)

from app.exceptions.custom_exceptions import (
    UserAlreadyExistsException,
    UserNotFoundException,
    InvalidCredentialsException,
    InvalidTokenException,
    NoteNotFoundException
)

app = FastAPI()

app.add_exception_handler(
    UserAlreadyExistsException,
    user_exists_handler
)

app.add_exception_handler(
    UserNotFoundException,
    user_not_found_handler
)

app.add_exception_handler(
    InvalidCredentialsException,
    invalid_credentials_handler
)

app.add_exception_handler(
    InvalidTokenException,
    invalid_token_handler
)

app.add_exception_handler(
    NoteNotFoundException,
    note_not_found_handler
)

# Register Routers
app.include_router(auth_router)
app.include_router(note_router)

# Create Database Tables
Base.metadata.create_all(bind=engine)