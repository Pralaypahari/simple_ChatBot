from langchain_community.tools import DuckDuckGoSearchRun
from langchain.tools import tool

web_search = DuckDuckGoSearchRun()

@tool
def search_the_web(query: str) -> str:
    """
    use this tool to search the web
    """
    return web_search.invoke(query)
