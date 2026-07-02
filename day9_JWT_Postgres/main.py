from fastapi import FastAPI

from database import Base, engine, SessionLocal
from models import User, Note

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
#Base.metadata.create_all(bind=engine)

@app.get("/debug/users")
def debug_users():
    db = SessionLocal()

    users = db.query(User).all()

    data = [
        {
            "id": u.id,
            "username": u.username,
            "role": u.role
        }
        for u in users
    ]

    db.close()

    return data


@app.post("/debug/make-admin/{username}")
def make_admin(username: str):
    db = SessionLocal()

    user = (
        db.query(User)
        .filter(User.username == username)
        .first()
    )

    if not user:
        db.close()
        return {"error": "User not found"}

    user.role = "admin"

    db.commit()
    db.refresh(user)

    db.close()

    return {
        "message": f"{username} is now admin"
    }