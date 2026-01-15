from src.agents.chat_agent.states.chat_agent_state import ChatAgentState
from src.agents.chat_agent.tools.date_time import get_current_date_and_time
from langchain.messages import ToolMessage

tools = [
    get_current_date_and_time
]

tools_by_name = {tool.name: tool for tool in tools}

def tool_executor(state: ChatAgentState) -> ChatAgentState:
    """
    """
    result = []
    for tool_call in state["messages"][-1].tool_calls:
        tool = tools_by_name[tool_call["name"]]
        observation = tool.invoke(tool_call["args"])

        result.append(
            ToolMessage(
                content = observation,
                tool_call_id = tool_call["id"]
            )
        )
    return {"messages": result}