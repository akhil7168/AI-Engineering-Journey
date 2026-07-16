import json

from database import SessionLocal

from app.core.redis import redis_client
from app.core.logging_config import logger

from app.services.conversation_db_service import (
    load_conversation,
    save_message,
    delete_conversation
)


CACHE_EXPIRY = 3600


def get_cache_key(session_id: str):

    return f"chat:{session_id}"


def get_conversation(session_id: str):

    cache_key = get_cache_key(session_id)

    cached_data = redis_client.get(cache_key)

    if cached_data:

        logger.info(
            f"REDIS HIT : {session_id}"
        )

        return json.loads(cached_data)

    logger.info(
        f"REDIS MISS : {session_id}"
    )

    db = SessionLocal()

    try:

        conversation = load_conversation(
            db,
            session_id
        )

        logger.info(
            f"POSTGRES LOADED {len(conversation)} messages"
        )

        redis_client.setex(
            cache_key,
            CACHE_EXPIRY,
            json.dumps(conversation)
        )

        logger.info(
            "CACHE REFRESHED"
        )

        return conversation

    finally:

        db.close()


def save_conversation(
    session_id: str,
    conversation: list
):

    cache_key = get_cache_key(session_id)

    redis_client.setex(
        cache_key,
        CACHE_EXPIRY,
        json.dumps(conversation)
    )

    logger.info(
        f"Conversation cached : {session_id}"
    )


def add_user_message(
    conversation,
    prompt
):

    conversation.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    return conversation


def add_ai_message(
    conversation,
    response
):

    conversation.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    return conversation


def persist_messages(
    session_id: str,
    user_prompt: str,
    ai_response: str
):

    db = SessionLocal()

    try:

        save_message(
            db,
            session_id,
            "user",
            user_prompt
        )

        save_message(
            db,
            session_id,
            "assistant",
            ai_response
        )

        logger.info(
            "Conversation stored in PostgreSQL"
        )

    finally:

        db.close()


def clear_conversation(
    session_id: str
):

    cache_key = get_cache_key(session_id)

    redis_client.delete(cache_key)

    db = SessionLocal()

    try:

        delete_conversation(
            db,
            session_id
        )

        logger.info(
            f"Conversation deleted : {session_id}"
        )

    finally:

        db.close()