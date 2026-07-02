from fastapi import HTTPException

from models import (
    User,
    Note
)
from app.exceptions.custom_exceptions import (
    NoteNotFoundException
)

import json

from app.core.redis import redis_client

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
    cache_key = f"notes_{db_user.id}"
    redis_client.delete(cache_key)
    print("CACHE INVALIDATED")


    return {
        "message": "Note Created"
    }

def get_notes_service(db, db_user):

    cache_key = f"notes_{db_user.id}"

    # Check Redis first
    cached_notes = redis_client.get(cache_key)

    if cached_notes:
        print("CACHE HIT")
        return json.loads(cached_notes)

    print("CACHE MISS")

    # Query PostgreSQL
    notes = (
        db.query(Note)
        .filter(Note.user_id == db_user.id)
        .all()
    )

    # Convert SQLAlchemy objects to dictionaries
    notes_data = [
    {
        "id": note.id,
        "title": note.title,
        "content": note.content,
        "user_id": note.user_id
    }
    for note in notes
]

    # Store in Redis for 60 seconds
    redis_client.setex(
        cache_key,
        60,
        json.dumps(notes_data)
    )

    return notes_data