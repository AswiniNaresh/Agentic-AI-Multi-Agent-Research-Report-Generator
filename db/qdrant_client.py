from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
from config import QDRANT_URL, QDRANT_API_KEY

COLLECTION_NAME = "documents"

# Try to connect to remote Qdrant server, fallback to in-memory for local development
try:
    if QDRANT_URL and QDRANT_API_KEY:
        client = QdrantClient(
            url=QDRANT_URL,
            api_key=QDRANT_API_KEY,
            timeout=10.0
        )
        # Test connection
        client.get_collections()
        print("✓ Connected to remote Qdrant server")
    else:
        raise ValueError("QDRANT_URL or QDRANT_API_KEY not set")
except Exception as e:
    print(f"⚠ Could not connect to remote Qdrant: {e}")
    print("→ Using in-memory Qdrant for local development")
    client = QdrantClient(":memory:")

def create_collection():
    try:
        client.recreate_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(size=384, distance=Distance.COSINE),
        )
    except Exception as e:
        print(f"Error creating collection: {e}")
        # Try to create if it doesn't exist
        try:
            client.create_collection(
                collection_name=COLLECTION_NAME,
                vectors_config=VectorParams(size=384, distance=Distance.COSINE),
            )
        except Exception as create_error:
            print(f"Error creating collection: {create_error}")