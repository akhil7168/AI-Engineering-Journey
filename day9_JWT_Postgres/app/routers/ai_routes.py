from fastapi import APIRouter

from schemas import (
    ConversationRequest,
    ConversationResponse
)

from app.services.ai_service import generate_ai_response

from app.services.memory_service import (
    get_conversation,
    clear_conversation
)
from database import SessionLocal
from app.services.conversation_db_service import(list_conversations,load_conversation,delete_conversation)

router = APIRouter(
    prefix="/ai",
    tags=["AI"]
)


@router.post(
    "/chat",
    response_model=ConversationResponse,
    summary="Chat with AI",
    description="Chat with AI using conversation memory."
)
async def chat(
    request: ConversationRequest
):

    response = generate_ai_response(
        session_id=request.session_id,
        prompt=request.prompt,
        mode=request.mode
    )

    return ConversationResponse(
        session_id=request.session_id,
        response=response
    )


@router.get(
    "/history/{session_id}",
    summary="Get Conversation History"
)
def get_history(
    session_id: str
):

    conversation = get_conversation(session_id)

    return {
        "session_id": session_id,
        "messages": conversation
    }


@router.delete(
    "/history/{session_id}",
    summary="Clear Conversation"
)
def delete_history(
    session_id: str
):

    clear_conversation(session_id)

    return {
        "message": "Conversation cleared successfully."
    }

@router.get(
    "/conversations",
    summary="Get All Conversations"
)
def get_all_conversations():

    db = SessionLocal()

    try:

        conversations = list_conversations(db)

        return [
            {
                "id": conversation.id,
                "session_id": conversation.session_id,
                "created_at": conversation.created_at
            }
            for conversation in conversations
        ]

    finally:

        db.close()

@router.get(
    "/conversation/{session_id}",
    summary="Get Conversation"
)
def get_conversation_history(
    session_id: str
):

    db = SessionLocal()

    try:

        messages = load_conversation(
            db,
            session_id
        )

        return {
            "session_id": session_id,
            "messages": messages
        }

    finally:

        db.close()

@router.delete(
    "/conversation/{session_id}",
    summary="Delete Conversation"
)
def delete_conversation_history(
    session_id: str
):

    clear_conversation(session_id)

    return {
        "message": "Conversation deleted successfully."
    }