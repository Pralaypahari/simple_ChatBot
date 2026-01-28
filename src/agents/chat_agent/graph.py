from src.agents.chat_agent.states.chat_agent_state import ChatAgentState
from src.agents.chat_agent.node.chat_node import chat
from src.agents.chat_agent.node.should_continue import should_continue
from src.agents.chat_agent.node.tool_executor_node import tool_executor
from langgraph.graph import START, END, StateGraph
from langgraph.graph.state import CompiledStateGraph
from src.services.database_services import db_manager


def create_chat_agent_graph() -> CompiledStateGraph:
    """
    """
    graph_builder = StateGraph(ChatAgentState)

    graph_builder.add_node("chat_node", chat)
    graph_builder.add_node("tool_executor_node", tool_executor)

    graph_builder.add_edge(START, "chat_node")
    graph_builder.add_conditional_edges("chat_node", should_continue)
    graph_builder.add_edge("tool_executor_node", "chat_node")

    checkpointer = db_manager.get_saver()

    return graph_builder.compile(checkpointer = checkpointer)