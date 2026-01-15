from typing import Literal
from langgraph.graph import END
from src.agents.chat_agent.states.chat_agent_state import ChatAgentState

def should_continue(state: ChatAgentState) -> ChatAgentState:
    """
    decide if we should continue the loop or stop based upon whether the LLM made a tool call
    """
    messages = state["messages"]
    last_message = messages[-1]

    if last_message.tool_calls: return "tool_executor_node"

    return END