from fastapi import APIRouter
from src.handlers.chat_handler import chat_handler
from langchain.messages import AnyMessage
router = APIRouter()

@router.post("/chat")
def chat_with_ai(message: str) -> dict[str, list[AnyMessage]]:
    '''
    '''
    return chat_handler(message=message)
    