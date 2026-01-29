from src.agents.chat_agent.states.chat_agent_state import ChatAgentState
from langchain_core.prompts import ChatPromptTemplate
from src.agents.chat_agent.tools.date_time import get_current_date_and_time
from src.agents.chat_agent.tools.web_search_tool import web_search, search_the_web
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv(override = True)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

template = """
you are a professional chat assistant answer only in short but precise manner only in english language

Message hitory:
{message_history}
"""

def chat(state: ChatAgentState) -> ChatAgentState:
    '''
    '''
    prompt_template = ChatPromptTemplate.from_template(template = template)
    model = ChatGroq(
        model="openai/gpt-oss-120b",
        api_key = GROQ_API_KEY
    )

    model = model.bind_tools(
        tools = [
            get_current_date_and_time,
            search_the_web
        ]
    )
    chain = prompt_template | model

    answer = chain.invoke(state["messages"])
    return {
        "messages": [answer]
    }