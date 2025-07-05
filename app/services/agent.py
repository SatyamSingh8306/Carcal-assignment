from langchain_groq import ChatGroq
from langchain_community.tools import TavilySearchResults
from langchain.agents import initialize_agent, AgentType
from app import GROQ_MODEL , GROQ_API_KEY, TAVILY_API_KEY

_llm = ChatGroq(model=GROQ_MODEL,
    api_key = GROQ_API_KEY)  # You can also use "mixtral-8x7b-32768" if needed

search_tool = TavilySearchResults(max_results=3,tavily_api_key = TAVILY_API_KEY)


tools = [search_tool]


agent = initialize_agent(
    tools=tools,
    llm=_llm,
    agent=AgentType.OPENAI_FUNCTIONS,  # Use function-calling style agent
    verbose=True
)

