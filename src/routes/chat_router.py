from fastapi import APIRouter
from src.handlers.chat_handler import chat_handler
from src.handlers.chat_handler import chat_history_handler
from src.handlers.chat_handler import get_all_threads_handler
from langchain.messages import AnyMessage
from src.agents.chat_agent.states.chat_agent_state import ChatAgentState

router = APIRouter()

@router.post("/chat/{thread_id}")
def chat_with_ai(thread_id: str, message: str) -> ChatAgentState:
    '''
    '''
    return chat_handler(thread_id = thread_id, message=message)

@router.get("/chat/threads")
def get_all_threads() ->list[str]:
    """
    """
    return get_all_threads_handler()

@router.get("/chat/history/{thread_id}")
def get_chat_history(thread_id: str):
    """
    """
    return chat_history_handler(thread_id = thread_id)