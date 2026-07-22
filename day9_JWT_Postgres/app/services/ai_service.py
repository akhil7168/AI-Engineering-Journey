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

from app.ai.retriever import retrieve_context

from app.services.memory_service import (
    get_conversation,
    save_conversation,
    add_user_message,
    add_ai_message,
    persist_messages
)

from app.core.logging_config import logger


def build_rag_prompt(question: str) -> str:
    """
    Build a Retrieval-Augmented prompt.
    """

    context = retrieve_context(question)

    if not context.strip():
        context = "No relevant information was retrieved from the knowledge base."

    return f"""
You are an AI Backend Engineering Assistant.

Instructions:

1. Use the retrieved context whenever possible.
2. If the context is insufficient, clearly state that and answer from your own knowledge.
3. Be concise and technically accurate.

==============================
RETRIEVED CONTEXT
==============================

{context}

==============================
QUESTION
==============================

{question}

==============================
ANSWER
==============================
"""


def get_system_prompt(mode: str) -> str:

    if mode == "backend":
        return BACKEND_PROMPT

    if mode == "python":
        return PYTHON_PROMPT

    if mode == "interviewer":
        return INTERVIEWER_PROMPT

    return GENERAL_PROMPT


def build_messages(
    conversation: list,
    system_prompt: str,
    rag_prompt: str
):

    messages = [
        {
            "role": "system",
            "content": system_prompt
        }
    ]

    messages.extend(conversation)

    for i in range(len(messages) - 1, -1, -1):
        if messages[i]["role"] == "user":
            messages[i]["content"] = rag_prompt
            break

    return messages


def generate_ai_response(
    session_id: str,
    prompt: str,
    mode: str = "general"
):

    logger.info("=" * 60)
    logger.info("NEW AI REQUEST")

    system_prompt = get_system_prompt(mode)

    conversation = get_conversation(session_id)

    rag_prompt = build_rag_prompt(prompt)

    conversation = add_user_message(
        conversation,
        prompt
    )

    messages = build_messages(
        conversation,
        system_prompt,
        rag_prompt
    )

    try:

        response = chat_with_ai(messages)

        conversation = add_ai_message(
            conversation,
            response
        )

        save_conversation(
            session_id,
            conversation
        )

        persist_messages(
            session_id,
            prompt,
            response
        )

        return response

    except Exception as e:

        logger.exception(e)

        return "Unable to generate AI response."


def generate_streaming_response(
    session_id: str,
    prompt: str,
    mode: str = "general"
):

    logger.info("=" * 60)
    logger.info("STREAMING REQUEST")

    system_prompt = get_system_prompt(mode)

    conversation = get_conversation(session_id)

    rag_prompt = build_rag_prompt(prompt)

    conversation = add_user_message(
        conversation,
        prompt
    )

    messages = build_messages(
        conversation,
        system_prompt,
        rag_prompt
    )

    complete_response = ""

    try:

        for token in stream_chat_with_ai(messages):

            complete_response += token

            yield token

        conversation = add_ai_message(
            conversation,
            complete_response
        )

        save_conversation(
            session_id,
            conversation
        )

        persist_messages(
            session_id,
            prompt,
            complete_response
        )

    except Exception as e:

        logger.exception(e)

        yield "Unable to generate AI response."