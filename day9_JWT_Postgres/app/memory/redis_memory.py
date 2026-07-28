import json

from app.core.redis import redis_client
from app.memory.conversation_memory import ConversationMemory


class RedisMemoryStore:
    """
    Stores ConversationMemory in Redis.
    """

    def __init__(self):

        self.redis = redis_client

    def _key(
        self,
        session_id: str
    ):

        return f"memory:{session_id}"

    # =====================================================
    # Save Memory
    # =====================================================

    def save_memory(
        self,
        session_id: str,
        memory: ConversationMemory
    ):

        self.redis.set(

            self._key(session_id),

            json.dumps(
                memory.to_dict()
            )

        )

    # =====================================================
    # Load Memory
    # =====================================================

    def load_memory(
        self,
        session_id: str
    ):

        data = self.redis.get(

            self._key(session_id)

        )

        if data is None:

            return ConversationMemory()

        return ConversationMemory.from_dict(

            json.loads(data)

        )

    # =====================================================
    # Delete Memory
    # =====================================================

    def delete_memory(
        self,
        session_id: str
    ):

        self.redis.delete(

            self._key(session_id)

        )

    # =====================================================
    # Check Existence
    # =====================================================

    def exists(
        self,
        session_id: str
    ):

        return self.redis.exists(

            self._key(session_id)

        )