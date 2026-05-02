from agents.llm import groq_llm

def plan(query):
    return groq_llm(f"Break into sub-questions:\n{query}").split("\n")