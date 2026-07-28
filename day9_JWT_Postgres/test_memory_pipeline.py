from app.memory.memory_manager import MemoryManager


SESSION = "akhil"

print("=" * 70)
print("DAY 42 - MEMORY PIPELINE TEST")
print("=" * 70)

manager = MemoryManager()

# --------------------------------------------------
# Load previous memory
# --------------------------------------------------

manager.load_from_redis(SESSION)

print("\nLoaded Previous Memory")
print("-" * 40)
print(manager.get_messages())

# --------------------------------------------------
# Simulate Conversation
# --------------------------------------------------

manager.add_user_message(
    "Hello!"
)

manager.add_assistant_message(
    "Hi! How can I help you?"
)

manager.add_user_message(
    "Explain JWT Authentication."
)

manager.add_assistant_message(
    "JWT is a secure token used for authentication."
)

manager.add_user_message(
    "How do Refresh Tokens work?"
)

# --------------------------------------------------
# Show Current Memory
# --------------------------------------------------

print("\nConversation")
print("-" * 40)

for msg in manager.get_messages():

    print(msg)

# --------------------------------------------------
# Build Context
# --------------------------------------------------

context = manager.get_context(
    "Can you give me an example?"
)

print("\nGenerated Context")
print("-" * 40)

for message in context:

    print(message)

# --------------------------------------------------
# Optimize Memory
# --------------------------------------------------

manager.optimize()

print("\nMemory Statistics")
print("-" * 40)

print(manager.memory_statistics())

# --------------------------------------------------
# Save
# --------------------------------------------------

manager.save_to_redis(SESSION)

print("\nSaved Successfully")

# --------------------------------------------------
# Reload
# --------------------------------------------------

reload_manager = MemoryManager()

reload_manager.load_from_redis(SESSION)

print("\nReloaded Messages")
print("-" * 40)

for msg in reload_manager.get_messages():

    print(msg)

print("\nSummary")
print("-" * 40)

print(reload_manager.get_summary())

print("\nDAY 42 COMPLETED")