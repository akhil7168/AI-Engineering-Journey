from typing import List, Dict

from app.ai.client import chat_with_ai, stream_chat_with_ai
from app.ai.retriever import retrieve_context

from app.agents.agent_state import AgentState
from app.agents.planner import Planner
from app.agents.workflow import WorkflowEngine
from app.agents.response_generator import ResponseGenerator

from app.services.memory_service import (
    get_conversation,
    save_conversation,
    persist_messages,
    add_user_message,
    add_ai_message
)

from app.services.agent_state_service import AgentStateService

# --------------------------------------------------
# Agent Components
# --------------------------------------------------

planner = Planner()

workflow = WorkflowEngine()

response_generator = ResponseGenerator()

def execute_agent_workflow(prompt: str):
    """
    Executes the complete multi-step agent workflow.

    Planner
        ↓
    Workflow Engine
        ↓
    Response Generator
    """

    state = AgentState(query=prompt)

    planner.create_plan(state)

    AgentStateService.save_state(
    "workflow",
    state
    )

    workflow.execute(state)

    AgentStateService.save_state(
    "workflow",
    state
    )

    response = response_generator.generate(state)

    AgentStateService.save_state(
    "workflow",
    state
    )

    return {

        "state": state,

        "response": response,

        "planned_tools": state.planned_tools,

        "completed_tools": state.completed_tools,

        "errors": state.errors

    }


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

    Flow

    User
        ↓
    Planner
        ↓
    Workflow Engine
        ↓
    Response Generator
        ↓
    OR
        ↓
    RAG + LLM
    """

    # --------------------------------------------------
    # Execute Planner + Workflow
    # --------------------------------------------------

    workflow_result = execute_agent_workflow(prompt)

    state = workflow_result["state"]

    # --------------------------------------------------
    # If at least one real tool executed,
    # return the combined response.
    # --------------------------------------------------

    real_tools = [

        tool

        for tool in state.completed_tools

        if tool != "llm"

    ]

    if len(real_tools) > 0:

        response = workflow_result["response"]

        conversation = get_conversation(
            session_id
        )

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
    # Fallback to RAG + LLM
    # --------------------------------------------------

    conversation = get_conversation(
        session_id
    )

    context = retrieve_context(
        prompt,
        top_k=5
    )

    rag_prompt = build_rag_prompt(
        question=prompt,
        context=context
    )

    messages = build_messages(

        system_prompt=get_system_prompt(mode),

        conversation=conversation,

        user_prompt=rag_prompt

    )

    response = chat_with_ai(
        messages
    )

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
    Planner
        ↓
    Workflow Engine
        ↓
    Response Generator
        ↓
    OR
        ↓
    RAG + Ollama Streaming
    """

    # --------------------------------------------------
    # Execute Planner + Workflow
    # --------------------------------------------------

    workflow_result = execute_agent_workflow(prompt)

    state = workflow_result["state"]

    # --------------------------------------------------
    # If at least one real tool executed,
    # return the combined response immediately.
    # --------------------------------------------------

    real_tools = [

        tool

        for tool in state.completed_tools

        if tool != "llm"

    ]

    if len(real_tools) > 0:

        response = workflow_result["response"]

        conversation = get_conversation(
            session_id
        )

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
    # Save Conversation
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