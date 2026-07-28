import ollama

from app.core.logging_config import logger

MODEL_NAME = "gemma2:2b"



def chat_with_ai(messages: list):
    """
    Normal AI response.
    Returns the complete response as a string.
    """

    try:

        response = ollama.chat(
            model=MODEL_NAME,
            messages=messages,
            stream=False
        )

        return response["message"]["content"]

    except Exception as e:

        logger.error(f"Ollama Error: {str(e)}")

        raise e


def stream_chat_with_ai(messages: list):
    """
    Stream AI response from Ollama.
    """

    logger.info("Connecting to Ollama...")

    try:

        stream = ollama.chat(
            model=MODEL_NAME,
            messages=messages,
            stream=True
        )

        logger.info("Connected to Ollama")

        for chunk in stream:

            if (
                "message" in chunk
                and "content" in chunk["message"]
            ):

                token = chunk["message"]["content"]

                if token:

                    yield token

        logger.info("Ollama Stream Finished")

    except Exception as e:

        logger.error(
            f"Ollama Streaming Error : {str(e)}"
        )

        raise