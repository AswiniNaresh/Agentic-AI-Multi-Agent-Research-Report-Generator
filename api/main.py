from fastapi import FastAPI
from workflows.graph import build_graph

app = FastAPI()
graph = build_graph()

@app.get("/")
def root():
    return {"message": "Agentic AI running"}

@app.get("/research")
def research(query: str):
    result = graph.invoke({"query": query})
    return {"result": result["final"]}