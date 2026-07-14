from pydantic import BaseModel,Field
from typing import Literal

class UserCreate(BaseModel):

    username: str

    password: str

class NoteCreate(BaseModel):

    title:str

    content:str

class NoteUpdate(BaseModel):
    title: str
    content: str

class NoteResponse(BaseModel):
    id: int
    title: str
    content: str
    user_id: int

    class Config:
        from_attributes = True

class UserResponse(BaseModel):
    id: int
    username: str
    role: str

    class Config:
        from_attributes = True

class ChatRequest(BaseModel):
    prompt: str = Field(
        ...,
        min_length=1,
        max_length=1000,
        description="Prompt to send to Gemini AI"
    )

    mode: Literal[
        "general",
        "backend",
        "python",
        "interviewer"
    ] = Field(
        default="general",
        description="Choose the AI personality"
    )


class ChatResponse(BaseModel):
    response: str
    