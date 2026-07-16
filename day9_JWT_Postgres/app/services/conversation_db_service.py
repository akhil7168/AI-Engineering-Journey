from sqlalchemy.orm import Session

from models import (
    Conversation,
    ChatMessage
)
from app.core.logging_config import logger

def get_conversation_by_session(
    db,
    session_id: str
):

    logger.info(
        f"Searching conversation: {session_id}"
    )

    conversation = (
        db.query(Conversation)
        .filter(
            Conversation.session_id == session_id
        )
        .first()
    )

    if conversation:

        logger.info(
            "Conversation found in PostgreSQL"
        )

    else:

        logger.info(
            "Conversation does not exist"
        )

    return conversation


def create_conversation(
    db,
    session_id: str
):

    logger.info(
        f"Creating conversation: {session_id}"
    )

    conversation = Conversation(
        session_id=session_id
    )

    db.add(conversation)

    db.commit()

    db.refresh(conversation)

    logger.info(
        "Conversation created successfully"
    )

    return conversation


def get_or_create_conversation(
    db: Session,
    session_id: str
):

    conversation = get_conversation_by_session(
        db,
        session_id
    )

    if conversation:
        return conversation

    return create_conversation(
        db,
        session_id
    )


def save_message(
    db,
    session_id: str,
    role: str,
    content: str
):

    conversation = get_or_create_conversation(
        db,
        session_id
    )

    logger.info(
        f"Saving {role} message"
    )

    message = ChatMessage(
        conversation_id=conversation.id,
        role=role,
        content=content
    )

    db.add(message)

    db.commit()

    db.refresh(message)

    logger.info(
        "Message saved successfully"
    )

    return message


def load_conversation(
    db,
    session_id: str
):

    logger.info(
        f"Loading conversation: {session_id}"
    )

    conversation = get_conversation_by_session(
        db,
        session_id
    )

    if not conversation:

        logger.info(
            "No conversation found"
        )

        return []

    messages = (
        db.query(ChatMessage)
        .filter(
            ChatMessage.conversation_id == conversation.id
        )
        .order_by(
            ChatMessage.created_at.asc()
        )
        .all()
    )

    logger.info(
        f"{len(messages)} messages loaded"
    )

    return [
        {
            "role": message.role,
            "content": message.content
        }
        for message in messages
    ]


def delete_conversation(
    db,
    session_id: str
):

    logger.info(
        f"Deleting conversation: {session_id}"
    )

    conversation = get_conversation_by_session(
        db,
        session_id
    )

    if not conversation:

        logger.warning(
            "Conversation not found"
        )

        return False

    db.delete(conversation)

    db.commit()

    logger.info(
        "Conversation deleted successfully"
    )

    return True


def list_conversations(
    db
):

    conversations = (
        db.query(Conversation)
        .order_by(
            Conversation.created_at.desc()
        )
        .all()
    )

    logger.info(
        f"{len(conversations)} conversations found"
    )

    return conversations