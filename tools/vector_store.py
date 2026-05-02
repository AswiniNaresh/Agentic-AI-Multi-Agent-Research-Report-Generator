from sentence_transformers import SentenceTransformer
from db.qdrant_client import client, COLLECTION_NAME

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed(text):
    return model.encode(text).tolist()

def add_documents(docs):
    points = []
    for i, doc in enumerate(docs):
        points.append({
            "id": i,
            "vector": embed(doc),
            "payload": {"text": doc}
        })
    client.upsert(collection_name=COLLECTION_NAME, points=points)