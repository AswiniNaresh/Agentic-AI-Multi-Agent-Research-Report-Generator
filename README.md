# Agentic-AI-Multi-Agent-Research-Report-Generator

I built an agentic AI system that can autonomously research a topic. It breaks a question into sub-tasks, retrieves information from both a vector database and the web, evaluates the quality of the data, and generates a structured response. It mimics how a human researches a topic rather than just answering directly

🚀 Overview

This project is an Agentic AI system that goes beyond traditional chatbots by planning, retrieving, analyzing, and refining answers autonomously.

Instead of directly answering a query, the system:

Breaks the problem into smaller tasks
Retrieves relevant information from multiple sources
Evaluates the quality of the information
Generates a structured, refined response
🧠 Core Idea

The system follows a multi-agent architecture, where each agent has a specific responsibility:

Planner Agent → Decomposes the query into sub-questions
Retriever Agent → Fetches data from:
Local knowledge base (vector search)
Web search (real-time information)
Analyst Agent → Extracts insights from retrieved data
Critic Agent → Validates and improves the answer
Writer Agent → Produces the final structured response
⚙️ Tech Stack
LLM: Groq (LLaMA3)
Vector Database: Qdrant
Web Search: Tavily
Orchestration: LangGraph
Backend: FastAPI
Embeddings: Sentence Transformers
🔍 How It Works
Step 1: Query Input

User sends a query:

"Compare vector databases for RAG systems"
Step 2: Planning

The Planner Agent breaks it into:

What is a vector database?
Key features comparison
Performance differences
Step 3: Retrieval (Hybrid Search)

The system retrieves data from:

🧠 Local Knowledge (Qdrant)
Documents are stored as embeddings
Semantic search retrieves relevant chunks
🌐 Web Knowledge (Tavily)
Used only when local data is insufficient
Fetches real-time and external information
Step 4: Analysis

The Analyst Agent:

Reads combined data
Extracts meaningful insights
Step 5: Self-Critique

The Critic Agent:

Checks completeness
Identifies missing information
Improves reasoning
Step 6: Final Output

The Writer Agent generates:

Structured
Coherent
Context-aware response
