from fastapi import FastAPI
from sqlalchemy.orm import Session

from database import SessionLocal
from database import engine

from models import Base
from models import Note

from schemas import NoteCreate

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/")
def home():

    return {
        "message": "Notes API Running"
    }


@app.post("/notes")
def create_note(note: NoteCreate):

    db: Session = SessionLocal()

    new_note = Note(
        title=note.title,
        content=note.content
    )

    db.add(new_note)

    db.commit()

    db.refresh(new_note)

    db.close()

    return new_note


@app.get("/notes")
def get_notes():

    db: Session = SessionLocal()

    notes = db.query(Note).all()

    db.close()

    return notes


@app.get("/notes/{note_id}")
def get_note(note_id: int):

    db = SessionLocal()

    note = db.query(Note).filter(Note.id == note_id).first()

    db.close()

    return note

@app.delete("/notes/{note_id}")
def delete_note(note_id: int):

    db = SessionLocal()

    note = db.query(Note).filter(Note.id == note_id).first()

    if note:

        db.delete(note)

        db.commit()

    db.close()

    return {
        "message": "Note deleted"
    }