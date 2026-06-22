from fastapi import Request
from fastapi.responses import JSONResponse

from app.exceptions.custom_exceptions import (
    UserAlreadyExistsException,
    UserNotFoundException,
    InvalidCredentialsException,
    InvalidTokenException,
    NoteNotFoundException
)

async def user_exists_handler(
    request: Request,
    exc: UserAlreadyExistsException
):
    return JSONResponse(
        status_code=400,
        content={
            "error": "User already exists"
        }
    )

async def user_not_found_handler(
    request: Request,
    exc: UserNotFoundException
):
    return JSONResponse(
        status_code=404,
        content={
            "error": "User not found"
        }
    )

async def invalid_credentials_handler(
    request: Request,
    exc: InvalidCredentialsException
):
    return JSONResponse(
        status_code=401,
        content={
            "error": "Invalid credentials"
        }
    )

async def invalid_token_handler(
    request: Request,
    exc: InvalidTokenException
):
    return JSONResponse(
        status_code=401,
        content={
            "error": "Invalid token"
        }
    )

async def note_not_found_handler(
    request: Request,
    exc: NoteNotFoundException
):
    return JSONResponse(
        status_code=404,
        content={
            "error": "Note not found"
        }
    )