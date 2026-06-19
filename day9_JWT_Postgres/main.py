from fastapi import FastAPI

from database import Base, engine

from app.routers.auth_routes import router as auth_router
from app.routers.note_routes import router as note_router

app = FastAPI()

# Register Routers
app.include_router(auth_router)
app.include_router(note_router)

# Create Database Tables
Base.metadata.create_all(bind=engine)