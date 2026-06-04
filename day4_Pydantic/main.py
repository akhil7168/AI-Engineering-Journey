from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Note(BaseModel):
    title: str
    content: str


@app.get("/")
def root():
    return {"message": "Pydantic Notes API"}

notes = []


@app.post("/notes")
def create_note(note: Note):

    notes.append(note)

    return {
        "message": "Note created"
    }

@app.get("/notes")
def get_notes():
    return notes

from typing import Optional

class Note(BaseModel):

    title:str

    content:str

    category: Optional[str] = None

{
  "title":"AI",
  "content":"Learning FastAPI"
}

{
  "title":"AI",
  "content":"Learning FastAPI",
  "category":"Programming"
}

class Message(BaseModel):
    message: str
    
@app.post(
    "/notes",
    response_model=Message
)
def create_note(note: Note):

    notes.append(note)

    return {
        "message":"Note created"
    }