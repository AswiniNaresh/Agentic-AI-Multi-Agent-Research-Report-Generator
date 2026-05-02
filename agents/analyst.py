from agents.llm import groq_llm

def analyze(context):
    return groq_llm(f"Extract key insights:\n{context}")