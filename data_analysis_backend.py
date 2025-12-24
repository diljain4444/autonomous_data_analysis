from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage,BaseMessage
from langgraph.graph import StateGraph,START,END
from langgraph.graph.message import add_messages
from typing import Annotated,TypedDict
import os
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

hf_key=os.environ["HUGGINGFACEHUB_API_TOKEN"]


llms = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    huggingfacehub_api_token=hf_key
)
model=ChatHuggingFace(llm=llms)

class state(TypedDict):
    messages:Annotated[list[BaseMessage],add_messages]

def chat_bot(state):
    response=model.invoke(state["messages"])
    return {"messages":response}

graph=StateGraph(state)
graph.add_node("chat_bot",chat_bot)
graph.add_edge(START,"chat_bot")
graph.add_edge("chat_bot",END)
workflow=graph.compile()

