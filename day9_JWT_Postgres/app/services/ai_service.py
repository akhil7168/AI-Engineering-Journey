from app.ai.client import chat_with_ai

from app.ai.prompts import (
    GENERAL_PROMPT,
    BACKEND_PROMPT,
    PYTHON_PROMPT,
    INTERVIEWER_PROMPT
)

from app.services.memory_service import (
    get_conversation,
    save_conversation,
    add_user_message,
    add_ai_message
)

from app.core.logging_config import logger


def generate_ai_response(
    session_id: str,
    prompt: str,
    mode: str = "general"
):
    """
    Handles the complete AI workflow:
    1. Select prompt template
    2. Load conversation history
    3. Append latest user message
    4. Send to LLM
    5. Save AI response
    """

    logger.info("=" * 60)
    logger.info("NEW AI REQUEST")
    logger.info(f"Session ID : {session_id}")
    logger.info(f"Mode       : {mode}")

    # Select Prompt
    if mode == "backend":
        system_prompt = BACKEND_PROMPT

    elif mode == "python":
        system_prompt = PYTHON_PROMPT

    elif mode == "interviewer":
        system_prompt = INTERVIEWER_PROMPT

    else:
        system_prompt = GENERAL_PROMPT

    logger.info("System Prompt Selected")

    # Load Conversation
    conversation = get_conversation(session_id)

    logger.info(
        f"Conversation Loaded ({len(conversation)} messages)"
    )

    # Add User Message
    conversation = add_user_message(
        conversation,
        prompt
    )

    # Build Complete Message List
    messages = [
        {
            "role": "system",
            "content": system_prompt
        }
    ]

    messages.extend(conversation)

    logger.info(
        f"Sending {len(messages)} messages to AI"
    )

    try:

        # Generate AI Response
        response = chat_with_ai(messages)

        logger.info("AI Response Generated")

        # Save AI Response
        conversation = add_ai_message(
            conversation,
            response
        )

        save_conversation(
            session_id,
            conversation
        )

        logger.info("Conversation Saved")
        logger.info("=" * 60)

        return response

    except Exception as e:

        logger.error(f"AI Error : {str(e)}")

        return "Unable to generate AI response."