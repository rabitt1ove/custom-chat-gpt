import sys
sys.path.append('/app')
 
from client.qdrant_manager import QdrantManager

# 類似度検索を実行
query = "検索ワード"
qdrant_manager = QdrantManager()
docs = qdrant_manager.qdrant.similarity_search(query=query, k=2)
for i in docs:
    print({"content": i.page_content, "metadata": i.metadata})
