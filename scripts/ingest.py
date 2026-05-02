import os
import sys
from pathlib import Path

# Add parent directory to path so imports work when running from scripts/
sys.path.insert(0, str(Path(__file__).parent.parent))

from pypdf import PdfReader
from tools.vector_store import add_documents
from db.qdrant_client import create_collection

DATA_PATH = "data"

def load_pdf(path):
    reader = PdfReader(path)
    return "\n".join([p.extract_text() or "" for p in reader.pages])

def load_txt(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def chunk(text, size=500, overlap=50):
    chunks = []
    i = 0
    while i < len(text):
        chunks.append(text[i:i+size])
        i += size - overlap
    return chunks

def load_docs():
    docs = []
    for f in os.listdir(DATA_PATH):
        path = os.path.join(DATA_PATH, f)

        if f.endswith(".pdf"):
            text = load_pdf(path)
        elif f.endswith(".txt"):
            text = load_txt(path)
        else:
            continue

        docs.extend(chunk(text))
    return docs

if __name__ == "__main__":
    create_collection()
    docs = load_docs()
    print(f"Loaded {len(docs)} chunks")
    add_documents(docs)
    print("Ingestion complete")