from app.ai.client import chat_with_ai

from app.ai.prompts import (
    GENERAL_PROMPT,
    BACKEND_PROMPT,
    PYTHON_PROMPT,
    INTERVIEWER_PROMPT
)

from app.core.logging_config import logger


def generate_ai_response(
    prompt: str,
    mode: str = "general"
):

    logger.info("=" * 60)
    logger.info("AI REQUEST RECEIVED")
    logger.info(f"Mode : {mode}")

    if mode == "backend":
        system_prompt = BACKEND_PROMPT

    elif mode == "python":
        system_prompt = PYTHON_PROMPT

    elif mode == "interviewer":
        system_prompt = INTERVIEWER_PROMPT

    else:
        system_prompt = GENERAL_PROMPT

    logger.info("Prompt Template Selected")

    try:

        response = chat_with_ai(
            system_prompt=system_prompt,
            user_prompt=prompt
        )

        logger.info("AI Response Generated Successfully")
        logger.info("=" * 60)

        return response

    except Exception as e:

        logger.error(f"AI Error : {e}")

        return "Unable to generate AI response."