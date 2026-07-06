from fastapi import Request
from fastapi.responses import JSONResponse

from app.exceptions.custom_exceptions import (
    UserAlreadyExistsException,
    UserNotFoundException,
    InvalidCredentialsException,
    InvalidTokenException,
    NoteNotFoundException
)
from app.core.logging_config import logger

async def user_exists_handler(
    request: Request,
    exc: UserAlreadyExistsException
):
    logger.warning("User already exists")

async def user_not_found_handler(
    request: Request,
    exc: UserNotFoundException
):
    logger.warning("User not found")

async def invalid_credentials_handler(
    request: Request,
    exc: InvalidCredentialsException
):
    logger.warning("Invalid credentials")

async def invalid_token_handler(
    request: Request,
    exc: InvalidTokenException
):
    logger.warning("Invalid token")

async def note_not_found_handler(
    request: Request,
    exc: NoteNotFoundException
):
    logger.warning("Note not found")