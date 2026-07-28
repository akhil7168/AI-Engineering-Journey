from app.ai.memory_chat import chat_with_memory

SESSION = "akhil"

response = chat_with_memory(
    SESSION,
    "What is JWT?"
)

print(response)

response = chat_with_memory(
    SESSION,
    "Explain it in simple words."
)

print(response)