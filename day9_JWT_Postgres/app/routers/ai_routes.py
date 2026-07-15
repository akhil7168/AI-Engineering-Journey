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