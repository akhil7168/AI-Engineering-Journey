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
class ChatMessage(BaseModel):
    role: Literal["user", "assistant"]
    content: str

class ChatResponse(BaseModel):
    response: str

class ConversationRequest(BaseModel):

    session_id: str = Field(
        ...,
        description="Unique conversation ID"
    )

    prompt: str = Field(
        ...,
        min_length=1,
        max_length=1000,
        description="Prompt sent to the AI"
    )

    mode: Literal[
        "general",
        "backend",
        "python",
        "interviewer"
    ] = "general"

class ConversationResponse(BaseModel):

    session_id: str

    response: str
    