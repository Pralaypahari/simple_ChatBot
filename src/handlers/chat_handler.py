from src.agents.chat_agent.graph import create_chat_agent_graph
from langchain.messages import HumanMessage, AnyMessage
from src.agents.chat_agent.states.chat_agent_state import ChatAgentState
from typing import Iterator


def chat_handler(thread_id: str, message: str) -> ChatAgentState:
    '''Recieves a message from user and sends it after modification

    Args:
    messages (str): the user message
    return:
    dict[str, str]: modified message
    '''
    graph = create_chat_agent_graph()

    return graph.invoke(
        input = {"messages": [HumanMessage(content = message)]
        },
        config = {
            "configurable": {
                "thread_id": thread_id
            }
        }
    )

def chat_stream_handler(thread_id: str, message: str) -> Iterator[str]:
    """
    """
    graph = create_chat_agent_graph()

    for chunk, metadata in graph.stream(
        input = {
            "messages": [HumanMessage(content = message)]
        },
        config = {
            "configurable": {
                "thread_id": thread_id
            }
        },
        stream_mode="messages"
    ):
        yield chunk.content


def get_all_threads_handler() -> list[str]:
    """
    """
    graph = create_chat_agent_graph()

    all_checkpoints = graph.checkpointer.list(config = {})

    threads = set()

    for checkpoint in all_checkpoints: 
        threads.add(checkpoint.config["configurable"]["thread_id"])
    return list(threads)


def chat_history_handler(thread_id: str):
    """
    """
    graph = create_chat_agent_graph()
    
    return graph.checkpointer.get(
        config = {
            "configurable": {
                "thread_id": thread_id
            }
        }
    )["channel_values"]
