from db.qdrant_client import client, COLLECTION_NAME
from tools.vector_store import embed

def search(query):
    try:
        results = client.query_points(
            collection_name=COLLECTION_NAME,
            query=embed(query),
            limit=3
        )
        texts = [r.payload["text"] for r in results.points]
        print(f"✓ Local search found {len(texts)} results for: {query}")
        return texts
    except Exception as e:
        print(f"⚠ Local search error: {e}")
        return []