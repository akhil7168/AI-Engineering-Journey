from app.ai.client import chat_with_ai
from app.memory.memory_manager import MemoryManager


memory = MemoryManager()


def chat_with_memory(
    session_id,
    query
):

    memory.load_from_redis(session_id)

    context = memory.get_context(query)

    response = chat_with_ai(context)

    memory.add_user_message(query)

    memory.add_assistant_message(response)

    memory.save_and_optimize(session_id)

    return response