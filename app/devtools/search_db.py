import sys
sys.path.append('/app')
 
from client.qdrant_manager import QdrantManager

# 引数の検索クエリを受け取る
textQuery = sys.argv[1] if len(sys.argv) > 1 and sys.argv[1].strip() else "default_text"
print(f"textQuery: {textQuery}")

# 検索クエリで類似度検索を実行
qdrant_manager = QdrantManager()
docs = qdrant_manager.qdrantNLP.similarity_search(query=textQuery, k=2)
for i in docs:
    print({"content": i.page_content, "metadata": i.metadata})
