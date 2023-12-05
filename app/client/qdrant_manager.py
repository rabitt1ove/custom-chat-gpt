from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
from langchain.vectorstores import Qdrant
from langchain.embeddings.openai import OpenAIEmbeddings

# Qdrantの設定
QDRANT_HOST = "qdrant"
QDRANT_PORT = 6333
COLLECTION_NAME = "my_collection"

class QdrantManager:
    def __init__(self):
        self.client = self._load_qdrant_client()
        self.gdrant = Qdrant(
            client=self.client,
            collection_name=COLLECTION_NAME,
            embeddings=OpenAIEmbeddings()
        )

    def _load_gdrant_client(self):
        client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)
        collections = client.get_collections().collections
        collection_names = [collection.name for collection in collections]
        if COLLECTION_NAME not in collection_names:
            client.create_collection(
                collection_name=COLLECTION_NAME,
                vectors_config=VectorParams(size=1536, distance=Distance.COSINE)
            )
        return client
