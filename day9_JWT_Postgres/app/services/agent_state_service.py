import json

from app.core.redis import redis_client

from app.agents.agent_state import AgentState


CACHE_EXPIRY = 3600


def get_agent_state_key(
    session_id: str
):

    return f"agent_state:{session_id}"


class AgentStateService:

    @staticmethod
    def save_state(
        session_id: str,
        state: AgentState
    ):

        redis_client.setex(

            get_agent_state_key(session_id),

            CACHE_EXPIRY,

            json.dumps(state.to_dict())

        )

    @staticmethod
    def load_state(
        session_id: str
    ):

        data = redis_client.get(

            get_agent_state_key(session_id)

        )

        if not data:

            return None

        if isinstance(data, bytes):

            data = data.decode()

        return json.loads(data)

    @staticmethod
    def delete_state(
        session_id: str
    ):

        redis_client.delete(

            get_agent_state_key(session_id)

        )