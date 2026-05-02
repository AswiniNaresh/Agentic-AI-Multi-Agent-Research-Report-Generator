from agents.llm import groq_llm

def critique(answer):
    return groq_llm(f"Check completeness:\n{answer}")