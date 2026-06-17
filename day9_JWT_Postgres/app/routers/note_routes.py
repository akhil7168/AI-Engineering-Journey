from fastapi import APIRouter, Depends, HTTPException

from models import User, Note
from schemas import (
    NoteCreate,
    NoteUpdate,
    NoteResponse
)
from database import SessionLocal
from auth import get_current_user


router = APIRouter(
    tags=["Notes"]
)


@router.get(
    "/notes",
    response_model=list[NoteResponse]
)
def get_notes(
    user=Depends(get_current_user)
):

    db = SessionLocal()

    db_user = get_db_user(
    db,
    user
    )

    notes = (
        db.query(Note)
        .filter(Note.user_id == db_user.id)
        .all()
    )

    db.close()

    return notes

@router.post("/notes")
def create_note(
    note: NoteCreate,
    user=Depends(get_current_user)
):

    db = SessionLocal()

    db_user = get_db_user(
    db,
    user
    )

    new_note = Note(
        title=note.title,
        content=note.content,
        user_id=db_user.id
    )

    db.add(new_note)
    db.commit()
    db.refresh(new_note)

    db.close()

    return {
        "message": "Note Created"
    }

@router.put("/notes/{note_id}")
def update_note(
    note_id: int,
    note: NoteUpdate,
    user=Depends(get_current_user)
):
    db = SessionLocal()

    db_user = get_db_user(
    db,
    user
    )

    db_note = (
        db.query(Note)
        .filter(Note.id == note_id, Note.user_id == db_user.id)
        .first()
    )

    if not db_note:
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )

    db_note.title = note.title
    db_note.content = note.content

    db.commit()

    db.close()

    return {
        "message": "Note Updated"
    }

@router.delete("/notes/{note_id}")
def delete_note(
    note_id: int,
    user=Depends(get_current_user)
):

    db = SessionLocal()

    db_user = get_db_user(
    db,
    user
    )
    db_note = (
        db.query(Note)
        .filter(
            Note.id == note_id,
            Note.user_id == db_user.id
        )
        .first()
    )

    if not db_note:
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )

    db.delete(db_note)

    db.commit()

    db.close()

    return {
        "message": "Note Deleted"
    }

def get_db_user(
    db,
    user
):
    username = user["sub"]

    return (
        db.query(User)
        .filter(User.username == username)
        .first()
    )