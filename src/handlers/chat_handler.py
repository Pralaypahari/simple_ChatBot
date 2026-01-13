from src.agents.chat_agent.graph import create_chat_agent_graph
from langchain.messages import HumanMessage, AnyMessage

def chat_handler(message: str) -> dict[str, list[AnyMessage]]:
    '''Recieves a message from user and sends it after modification

    Args:
    messages (str): the user message
    return:
    dict[str, str]: modified message
    '''
    graph = create_chat_agent_graph()
    return graph.invoke({"messages": [HumanMessage(content = message)]})
