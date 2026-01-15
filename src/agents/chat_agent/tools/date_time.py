import time
from langchain_core.tools import tool

@tool
def get_current_date_and_time() -> str:
    """
    use this to get current date and time
    """
    return time.ctime()
