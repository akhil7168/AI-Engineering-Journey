from fastapi import FastAPI

from database import Base, engine, SessionLocal
from models import *

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
from app.core.limiter import limiter
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from slowapi import _rate_limit_exceeded_handler
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from app.routers.admin_routes import router as admin_router
from app.routers.ai_routes import router as ai_router

app = FastAPI(
    title="AI Engineering Notes API",
    description="""
Production-ready Notes API built using FastAPI.

Features:
- JWT Authentication
- Role Based Access Control (RBAC)
- PostgreSQL Database
- Redis Caching
- Background Tasks
- Rate Limiting
- Logging & Monitoring
- Docker & Render Deployment
""",
    version="1.0.0",
    contact={
        "name": "Akhil Reddy",
        "email": "akhilpunyala@gmail.com"
    },
    license_info={
        "name": "MIT License"
    }
)

app.state.limiter = limiter

app.add_exception_handler(
    RateLimitExceeded,
    _rate_limit_exceeded_handler
)

app.add_middleware(SlowAPIMiddleware)

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
app.include_router(admin_router)
app.include_router(ai_router)

# Create Database Tables
Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "https://ai-engineering-journey.onrender.com"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=[
        "localhost",
        "127.0.0.1",
        "testserver",
        "*.onrender.com"
    ]
)
print("TrustedHostMiddleware configured")
print(app.user_middleware)

@app.middleware("http")
async def add_security_headers(request, call_next):

    response = await call_next(request)

    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    response.headers["Cache-Control"] = "no-store"

    return response

