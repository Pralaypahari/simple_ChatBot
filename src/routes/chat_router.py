from fastapi import APIRouter
from src.handlers.chat_handler import chat_handler
router = APIRouter()

@router.post("/chat")
def chat_with_ai(message: str) -> dict[str, str]:
    '''
    '''
    return chat_handler(message=message)
    