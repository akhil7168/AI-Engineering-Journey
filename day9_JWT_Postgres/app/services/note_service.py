import json

from models import (
    User,
    Note
)

from app.exceptions.custom_exceptions import (
    NoteNotFoundException
)

from app.core.redis import redis_client
from app.core.logging_config import logger


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

    logger.info(
        f"Note created by {db_user.username}"
    )

    cache_key = f"notes_{db_user.id}"

    redis_client.delete(cache_key)

    logger.info(
        "CACHE INVALIDATED"
    )

    return {
        "message": "Note Created"
    }


def get_notes_service(db, db_user):

    cache_key = f"notes_{db_user.id}"

    cached_notes = redis_client.get(cache_key)

    if cached_notes:
        logger.info("CACHE HIT")
        return json.loads(cached_notes)

    logger.info("CACHE MISS")

    notes = (
        db.query(Note)
        .filter(Note.user_id == db_user.id)
        .all()
    )

    notes_data = [
        {
            "id": note.id,
            "title": note.title,
            "content": note.content,
            "user_id": note.user_id
        }
        for note in notes
    ]

    redis_client.setex(
        cache_key,
        60,
        json.dumps(notes_data)
    )

    return notes_data