from fastapi import FastAPI

from app.routes.note_routes import router

app = FastAPI()

app.include_router(router)