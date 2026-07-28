from app.memory.conversation_memory import ConversationMemory


memory = ConversationMemory()

memory.add_message(

    "user",

    "Hello"

)

memory.add_message(

    "assistant",

    "Hi! How are you?"

)

memory.add_message(

    "user",

    "Tell me about JWT."

)

memory.add_message(

    "assistant",

    "JWT stands for JSON Web Token."

)

print("=" * 70)

print("ALL MESSAGES")

print("=" * 70)

print(memory.get_messages())

print()

print("=" * 70)

print("LAST TWO")

print("=" * 70)

print(memory.last_messages(2))

print()

memory.set_summary(

    "User greeted the assistant and asked about JWT."

)

print("=" * 70)

print("SUMMARY")

print("=" * 70)

print(memory.get_summary())

print()

print("=" * 70)

print("TOKEN COUNT")

print("=" * 70)

print(memory.token_count())

print()

print("=" * 70)

print("SERIALIZED")

print("=" * 70)

print(memory.to_dict())

print()

memory.remove_last_message()

print("=" * 70)

print("AFTER REMOVING LAST MESSAGE")

print("=" * 70)

print(memory.get_messages())

print()

memory.clear()

print("=" * 70)

print("AFTER CLEAR")

print("=" * 70)

print(memory.to_dict())