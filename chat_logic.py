from langchain.chat_models import ChatOpenAI
from langchain_groq import ChatGroq
from langchain.schema import HumanMessage, AIMessage, SystemMessage
from langgraph.graph import StateGraph
from typing import TypedDict, List
import os
import dotenv
dotenv.load_dotenv()

# LangChain LLM
# llm = ChatOpenAI(model="gpt-4", temperature=0.7)
llm = ChatGroq(
    model="llama3-8b-8192", 
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.7
)

# Define the chat state
class ChatState(TypedDict):
    messages: List
    user_input: str

# Nodes for LangGraph
def start_node(state: ChatState) -> ChatState:
    if not state["messages"]:
        state["messages"] = [SystemMessage(content="You are a helpful chatbot.")]
    state["messages"].append(HumanMessage(content=state["user_input"]))
    return state

def chat_node(state: ChatState) -> ChatState:
    response = llm(state["messages"])
    state["messages"].append(response)
    return state

# Create graph
graph = StateGraph(ChatState)
graph.add_node("start", start_node)
graph.add_node("chat", chat_node)

graph.set_entry_point("start")
graph.add_edge("start", "chat")

chatbot = graph.compile()
