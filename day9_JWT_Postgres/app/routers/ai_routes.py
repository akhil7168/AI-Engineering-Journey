from fastapi import APIRouter
from schemas import ChatRequest
from app.ai.client import chat_with_ai

router = APIRouter(
    prefix="/ai",
    tags=["Artificial Intelligence"]
)

@router.post("/chat")
async def chat(chat_request: ChatRequest):

    response = chat_with_ai(
        prompt=chat_request.prompt
    )

    return {
        "response": response
    }