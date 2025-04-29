from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.agents import initialize_agent
from langchain_community.tools import TavilySearchResults

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

search_tool = TavilySearchResults(search_depth="basic")
tools = [search_tool]

agent = initialize_agent(tools =tools, llm=llm,agent="zero-shot-react-description", verbose=True)
agent.invoke("When was SpaceX founded?")
# result = llm.invoke("Give me a fact about the Eiffel Tower.")
# print(result)
