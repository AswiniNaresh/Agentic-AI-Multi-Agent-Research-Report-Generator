from agents.llm import groq_llm

def write(notes):
    return groq_llm(f"Write structured report:\n{notes}")