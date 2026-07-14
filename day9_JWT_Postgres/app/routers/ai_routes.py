from fastapi import APIRouter

from schemas import ChatRequest

from app.services.ai_service import generate_ai_response

router = APIRouter(
    prefix="/ai",
    tags=["AI"]
)


@router.post(
    "/chat",
    summary="Chat with Local AI",
    description="Interact with the local Ollama model using different AI personalities."
)
async def chat(request: ChatRequest):

    response = generate_ai_response(
        prompt=request.prompt,
        mode=request.mode
    )

    return {
        "mode": request.mode,
        "response": response
    }