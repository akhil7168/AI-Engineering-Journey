from fastapi import HTTPException

from models import (
    User,
    Note
)

def create_note_service(
    db,
    note,
    db_user
):
    new_note = Note(
        title=note.title,
        content=note.content,
        user_id=db_user.id
    )

    db.add(new_note)

    db.commit()

    db.refresh(new_note)

    return {
        "message": "Note Created"
    }

def get_notes_service(
    db,
    db_user
):

    return (
        db.query(Note)
        .filter(
            Note.user_id == db_user.id
        )
        .all()
    )