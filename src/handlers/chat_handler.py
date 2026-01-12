from src.agents.chat_agent.graph import create_chat_agent_graph

def chat_handler(message: str) -> dict[str, str]:
    '''Recieves a message from user and sends it after modification

    Args:
    messages (str): the user message
    return:
    dict[str, str]: modified message
    '''
    graph = create_chat_agent_graph()
    return graph.invoke({"messages": message})
