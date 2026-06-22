from fastapi import APIRouter, Depends, HTTPException

from models import User, Note
from schemas import (
    NoteCreate,
    NoteUpdate,
    NoteResponse
)
from database import SessionLocal
from auth import get_current_user
from app.services.note_service import (
    create_note_service,
    get_notes_service
)
from app.exceptions.custom_exceptions import (
    NoteNotFoundException
)

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

    result = get_notes_service(
        db,
        db_user
    )

    db.close()

    return result

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

    result = create_note_service(
        db,
        note,
        db_user
    )

    db.close()

    return result

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
        raise NoteNotFoundException()

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
        raise NoteNotFoundException()

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