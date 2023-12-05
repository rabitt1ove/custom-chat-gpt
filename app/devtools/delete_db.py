import sys
sys.path.append('/app')

from client.qdrant_manager import QdrantManager, COLLECTION_NAME

qdrant_manager = QdrantManager()
qdrant_manager.client.delete_collection(collection_name=COLLECTION_NAME)
