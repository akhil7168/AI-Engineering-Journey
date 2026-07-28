from app.memory.memory_manager import MemoryManager

manager = MemoryManager()

memory = manager.get_memory()

memory.add_message(

    role="user",

    content="Hello AI"

)

memory.add_message(

    role="assistant",

    content="Hello! How can I help you today?"

)

print("=" * 60)

print("Conversation Memory")

print("=" * 60)

print(memory.to_dict())

print()

print("Message Count:")

print(memory.message_count())