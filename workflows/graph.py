from langgraph.graph import StateGraph
from typing import TypedDict, List

from agents.planner import plan
from agents.analyst import analyze
from agents.critic import critique
from agents.writer import write
from tools.retriever import search
from tools.web_search import tavily_search

class State(TypedDict):
    query: str
    plan: List[str]
    context: str
    analysis: str
    final: str

def planner_node(state):
    return {"plan": plan(state["query"])}

def retrieve_node(state):
    context = []

    for q in state["plan"]:
        local = search(q)
        context += local

        # Always perform web search to ensure comprehensive coverage
        web = tavily_search(q)
        context += [w.get("content", "") for w in web]

    return {"context": "\n".join(context)}

def analyze_node(state):
    return {"analysis": analyze(state["context"])}

def critique_node(state):
    feedback = critique(state["analysis"])
    return {"analysis": state["analysis"] + "\n\nCRITIQUE:\n" + feedback}

def write_node(state):
    return {"final": write(state["analysis"])}

def build_graph():
    builder = StateGraph(State)

    builder.add_node("planner", planner_node)
    builder.add_node("retrieve", retrieve_node)
    builder.add_node("analyze", analyze_node)
    builder.add_node("critique", critique_node)
    builder.add_node("write", write_node)

    builder.set_entry_point("planner")

    builder.add_edge("planner", "retrieve")
    builder.add_edge("retrieve", "analyze")
    builder.add_edge("analyze", "critique")
    builder.add_edge("critique", "write")

    return builder.compile()