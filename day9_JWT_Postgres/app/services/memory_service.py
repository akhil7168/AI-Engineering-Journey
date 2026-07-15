import json

from app.core.redis import redis_client
from app.core.logging_config import logger


def get_conversation(session_id: str):
    """
    Retrieve the complete conversation from Redis.
    Returns an empty list if no conversation exists.
    """

    cache_key = f"chat:{session_id}"

    conversation = redis_client.get(cache_key)

    if conversation:

        logger.info(
            f"Conversation loaded for session {session_id}"
        )

        return json.loads(conversation)

    logger.info(
        f"No conversation found for session {session_id}"
    )

    return []


def save_conversation(
    session_id: str,
    messages: list
):
    """
    Save the entire conversation back to Redis.
    """

    cache_key = f"chat:{session_id}"

    redis_client.setex(
        cache_key,
        3600,
        json.dumps(messages)
    )

    logger.info(
        f"Conversation saved for session {session_id}"
    )


def add_user_message(
    conversation: list,
    message: str
):
    """
    Add the user's message to the conversation.
    """

    conversation.append(
        {
            "role": "user",
            "content": message
        }
    )

    return conversation


def add_ai_message(
    conversation: list,
    message: str
):
    """
    Add the AI's response to the conversation.
    """

    conversation.append(
        {
            "role": "assistant",
            "content": message
        }
    )

    return conversation


def clear_conversation(
    session_id: str
):
    """
    Delete the conversation from Redis.
    """

    cache_key = f"chat:{session_id}"

    redis_client.delete(cache_key)

    logger.info(
        f"Conversation deleted for session {session_id}"
    )