from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from src.handlers.chat_handler import chat_handler
from src.handlers.chat_handler import chat_history_handler
from src.handlers.chat_handler import get_all_threads_handler
from src.handlers.chat_handler import chat_stream_handler
from langchain.messages import AnyMessage
from src.agents.chat_agent.states.chat_agent_state import ChatAgentState

router = APIRouter()

@router.post("/chat/{thread_id}")
def chat_with_ai(thread_id: str, message: str) -> ChatAgentState:
    '''
    '''
    return chat_handler(thread_id = thread_id, message=message)

@router.post("/stream/{thread_id}")
def stream_chat_with_ai(thread_id: str, message: str):
    """
    """
    return StreamingResponse(
        chat_stream_handler(thread_id = thread_id, message = message),
        media_type = "text/plain"
    )

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