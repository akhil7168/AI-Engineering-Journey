from app.ai.client import (
    chat_with_ai,
    stream_chat_with_ai
)

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
    add_ai_message,
    persist_messages
)

from app.core.logging_config import logger


def generate_ai_response(
    session_id: str,
    prompt: str,
    mode: str = "general"
):
    """
    Complete AI Workflow

    1. Load conversation (Redis → PostgreSQL if needed)
    2. Select system prompt
    3. Add latest user message
    4. Call AI
    5. Add AI response
    6. Update Redis cache
    7. Persist messages in PostgreSQL
    """

    logger.info("=" * 60)
    logger.info("NEW AI REQUEST")
    logger.info(f"Session ID : {session_id}")
    logger.info(f"Mode       : {mode}")

    # -------------------------
    # Select System Prompt
    # -------------------------

    if mode == "backend":
        system_prompt = BACKEND_PROMPT

    elif mode == "python":
        system_prompt = PYTHON_PROMPT

    elif mode == "interviewer":
        system_prompt = INTERVIEWER_PROMPT

    else:
        system_prompt = GENERAL_PROMPT

    logger.info("System Prompt Selected")

    # -------------------------
    # Load Conversation
    # -------------------------

    conversation = get_conversation(session_id)

    logger.info(
        f"Conversation Loaded ({len(conversation)} messages)"
    )

    # -------------------------
    # Add User Message
    # -------------------------

    conversation = add_user_message(
        conversation,
        prompt
    )

    # -------------------------
    # Prepare Messages
    # -------------------------

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

        # -------------------------
        # AI Response
        # -------------------------

        response = chat_with_ai(messages)

        logger.info(
            "AI Response Generated"
        )

        # -------------------------
        # Add AI Message
        # -------------------------

        conversation = add_ai_message(
            conversation,
            response
        )

        # -------------------------
        # Update Redis Cache
        # -------------------------

        save_conversation(
            session_id,
            conversation
        )

        logger.info(
            "Redis Cache Updated"
        )

        # -------------------------
        # Save to PostgreSQL
        # -------------------------

        persist_messages(
            session_id,
            prompt,
            response
        )

        logger.info(
            "Conversation Saved to PostgreSQL"
        )

        logger.info("=" * 60)

        return response

    except Exception as e:

        logger.error(
            f"AI Error : {str(e)}"
        )

        return "Unable to generate AI response."
    
def generate_streaming_response(
    session_id: str,
    prompt: str,
    mode: str = "general"
):
    """
    Streams AI response while maintaining
    conversation history.
    """

    logger.info("=" * 60)
    logger.info("STREAMING AI REQUEST")
    logger.info(f"Session ID : {session_id}")
    logger.info(f"Mode       : {mode}")

    # -------------------------
    # Select System Prompt
    # -------------------------

    if mode == "backend":
        system_prompt = BACKEND_PROMPT

    elif mode == "python":
        system_prompt = PYTHON_PROMPT

    elif mode == "interviewer":
        system_prompt = INTERVIEWER_PROMPT

    else:
        system_prompt = GENERAL_PROMPT

    logger.info("System Prompt Selected")

    # -------------------------
    # Load Conversation
    # -------------------------

    conversation = get_conversation(session_id)

    logger.info(
        f"Conversation Loaded ({len(conversation)} messages)"
    )

    # -------------------------
    # Add User Message
    # -------------------------

    conversation = add_user_message(
        conversation,
        prompt
    )

    # -------------------------
    # Prepare Messages
    # -------------------------

    messages = [
        {
            "role": "system",
            "content": system_prompt
        }
    ]

    messages.extend(conversation)

    logger.info(
        f"Sending {len(messages)} messages to Ollama"
    )

    complete_response = ""
    token_count = 0

    try:

        logger.info("Streaming Started")

        for token in stream_chat_with_ai(messages):

            complete_response += token
            token_count += 1

            yield token

        logger.info(
            f"Streaming Completed ({token_count} chunks)"
        )

        # -------------------------
        # Save Assistant Response
        # -------------------------

        conversation = add_ai_message(
            conversation,
            complete_response
        )

        logger.info("Assistant Message Added")

        # -------------------------
        # Save Redis
        # -------------------------

        save_conversation(
            session_id,
            conversation
        )

        logger.info("Conversation Cached in Redis")

        # -------------------------
        # Save PostgreSQL
        # -------------------------

        persist_messages(
            session_id,
            prompt,
            complete_response
        )

        logger.info("Conversation Saved to PostgreSQL")

        logger.info("=" * 60)

    except Exception as e:

        logger.error(
            f"Streaming Error : {str(e)}"
        )

        yield "Unable to generate AI response."