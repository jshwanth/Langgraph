from typing import List, Sequence
from dotenv import load_dotenv
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import END, MessageGraph
from chains import generation_chain,reflection_chain

load_dotenv()

# This script sets up a basic reflection and generation system using a MessageGraph.
# It imports necessary modules, loads environment variables, and defines two main functions:
# 1. `generate_node`: Invokes a generation chain with the current state messages.
# 2. `reflect_node`: Invokes a reflection chain with the current state messages and 
#    returns a list containing a HumanMessage with the response content.

graph = MessageGraph()
REFLECT = "reflect"
GENERATE = "generate"

def generate_node(state):
    generation_chain.invoke(
        {"messages":state["messages"]
    })

def reflect_node(state):
    response =  reflection_chain.invoke(
        {"messages":state["messages"]
    })
    return [HumanMessage(content=response.content)]

graph.add_node(GENERATE, generate_node)
graph.add_node(REFLECT, reflect_node)
graph.set_entrypoint(GENERATE)

def should_continue(state):
    if(len(state)>4):
        return END
    return REFLECT

graph.add_conditional_edge(GENERATE,should_continue)

graph.add_edge(REFLECT, GENERATE)

app = graph.compile()
# for visualization
print(app.get_graph().draw_mermaid())
app.get_graph().print_ascii()