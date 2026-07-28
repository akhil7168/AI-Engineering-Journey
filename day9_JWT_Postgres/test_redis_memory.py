from app.memory.memory_manager import MemoryManager

SESSION = "akhil"

manager = MemoryManager()

manager.add_user_message("Hello")

manager.add_assistant_message("Hi!")

manager.add_user_message("Explain JWT.")

manager.save_to_redis(SESSION)

print("=" * 60)
print("Saved")
print("=" * 60)

new_manager = MemoryManager()

new_manager.load_from_redis(SESSION)

print(new_manager.get_messages())

print()

print(new_manager.get_summary())

new_manager.delete_from_redis(SESSION)