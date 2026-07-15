from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

MODEL_NAME = "gemma3:1b"


def chat_with_ai(messages: list):
    """
    Sends the complete conversation to Ollama
    and returns the AI response.
    """

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        temperature=0.7
    )

    return response.choices[0].message.content