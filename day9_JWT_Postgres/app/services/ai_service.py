from typing import List, Dict

from app.ai.client import chat_with_ai, stream_chat_with_ai
from app.ai.retriever import retrieve_context

from app.agents.tool_selector import ToolSelector
from app.agents.tool_executor import ToolExecutor

from app.services.memory_service import (
    get_conversation,
    save_conversation,
    persist_messages,
    add_user_message,
    add_ai_message
)

# --------------------------------------------------
# Agent Initialization
# --------------------------------------------------

tool_selector = ToolSelector()
tool_executor = ToolExecutor()


# --------------------------------------------------
# Agent
# --------------------------------------------------

def execute_agent(prompt: str):
    """
    Executes a tool if the user's prompt matches one.
    Returns None if no suitable tool is found.
    """

    tool = tool_selector.select_tool(prompt)

    if tool is None:
        return None

    # ---------------- Calculator ----------------

    if tool == "calculator":

        expression = (
            prompt.replace("Calculate", "")
                  .replace("calculate", "")
                  .strip()
        )

        return tool_executor.execute(
            tool_name="calculator",
            expression=expression
        )

    # ---------------- Date & Time ----------------

    elif tool == "datetime":

        lower = prompt.lower()

        if "utc" in lower:
            action = "utc"

        elif "date" in lower:
            action = "date"

        elif "day" in lower:
            action = "day"

        elif "timestamp" in lower:
            action = "timestamp"

        elif "iso" in lower:
            action = "iso"

        else:
            action = "time"

        return tool_executor.execute(
            tool_name="datetime",
            action=action
        )

    # ---------------- Document Search ----------------

    elif tool == "document_search":

        return tool_executor.execute(
            tool_name="document_search",
            query=prompt
        )

    # ---------------- System Info ----------------

    elif tool == "system_info":

        return tool_executor.execute(
            tool_name="system_info"
        )

    return None


# --------------------------------------------------
# Prompt Helpers
# --------------------------------------------------

def get_system_prompt(mode: str) -> str:

    prompts = {

        "backend": (
            "You are an expert Backend Engineering tutor. "
            "Explain concepts clearly with practical examples."
        ),

        "dsa": (
            "You are an expert Data Structures and Algorithms tutor."
        ),

        "general": (
            "You are a helpful AI assistant."
        )

    }

    return prompts.get(mode, prompts["general"])


def build_rag_prompt(
    question: str,
    context: str
):

    if not context:

        return question

    return f"""
Use ONLY the following knowledge if relevant.

{context}

Question:
{question}
"""


def build_messages(
    system_prompt: str,
    conversation: List[Dict],
    user_prompt: str
):

    messages = [

        {
            "role": "system",
            "content": system_prompt
        }

    ]

    messages.extend(conversation)

    messages.append(

        {
            "role": "user",
            "content": user_prompt
        }

    )

    return messages

# --------------------------------------------------
# AI Response
# --------------------------------------------------

def generate_ai_response(
    session_id: str,
    prompt: str,
    mode: str = "general"
):
    """
    Main AI response pipeline.
    """

    # --------------------------------------------------
    # Agent Tools
    # --------------------------------------------------

    agent_response = execute_agent(prompt)

    if (
        agent_response
        and agent_response.get("success")
        and agent_response.get("tool") != "document_search"
    ):

        output = agent_response["output"]

        if isinstance(output, dict):

            if "result" in output:
                response = str(output["result"])
            else:
                response = str(output)

        else:

            response = str(output)

        conversation = get_conversation(session_id)

        conversation = add_user_message(
            conversation,
            prompt
        )

        conversation = add_ai_message(
            conversation,
            response
        )

        save_conversation(
            session_id,
            conversation
        )

        persist_messages(
            session_id,
            prompt,
            response
        )

        return response

    # --------------------------------------------------
    # Conversation
    # --------------------------------------------------

    conversation = get_conversation(
        session_id
    )

    # --------------------------------------------------
    # Retrieve Knowledge
    # --------------------------------------------------

    context = retrieve_context(
        prompt,
        top_k=5
    )

    rag_prompt = build_rag_prompt(
        prompt,
        context
    )

    # --------------------------------------------------
    # Build Messages
    # --------------------------------------------------

    messages = build_messages(
        system_prompt=get_system_prompt(mode),
        conversation=conversation,
        user_prompt=rag_prompt
    )

    # --------------------------------------------------
    # Call Ollama
    # --------------------------------------------------

    response = chat_with_ai(
        messages
    )

    # --------------------------------------------------
    # Update Memory
    # --------------------------------------------------

    conversation = add_user_message(
        conversation,
        prompt
    )

    conversation = add_ai_message(
        conversation,
        response
    )

    save_conversation(
        session_id,
        conversation
    )

    persist_messages(
        session_id,
        prompt,
        response
    )

    return response

# --------------------------------------------------
# Streaming AI Response
# --------------------------------------------------

def generate_streaming_response(
    session_id: str,
    prompt: str,
    mode: str = "general"
):
    """
    Streaming response pipeline.

    Flow

    User
        ↓
    Tool Selector
        ↓
    Tool
        ↓
    OR
        ↓
    RAG
        ↓
    Ollama Streaming
    """

    # --------------------------------------------------
    # Agent Tools
    # --------------------------------------------------

    agent_response = execute_agent(prompt)

    if (
        agent_response
        and agent_response.get("success")
        and agent_response.get("tool") != "document_search"
    ):

        output = agent_response["output"]

        if isinstance(output, dict):

            if "result" in output:

                response = str(output["result"])

            else:

                response = str(output)

        else:

            response = str(output)

        conversation = get_conversation(session_id)

        conversation = add_user_message(
            conversation,
            prompt
        )

        conversation = add_ai_message(
            conversation,
            response
        )

        save_conversation(
            session_id,
            conversation
        )

        persist_messages(
            session_id,
            prompt,
            response
        )

        yield response

        return

    # --------------------------------------------------
    # Load Conversation
    # --------------------------------------------------

    conversation = get_conversation(
        session_id
    )

    # --------------------------------------------------
    # Retrieve Context
    # --------------------------------------------------

    context = retrieve_context(
        prompt,
        top_k=5
    )

    rag_prompt = build_rag_prompt(
        question=prompt,
        context=context
    )

    # --------------------------------------------------
    # Build Messages
    # --------------------------------------------------

    messages = build_messages(

        system_prompt=get_system_prompt(mode),

        conversation=conversation,

        user_prompt=rag_prompt

    )

    # --------------------------------------------------
    # Stream Response
    # --------------------------------------------------

    complete_response = ""

    for token in stream_chat_with_ai(messages):

        complete_response += token

        yield token

    # --------------------------------------------------
    # Update Conversation
    # --------------------------------------------------

    conversation = add_user_message(
        conversation,
        prompt
    )

    conversation = add_ai_message(
        conversation,
        complete_response
    )

    save_conversation(
        session_id,
        conversation
    )

    persist_messages(
        session_id,
        prompt,
        complete_response
    )