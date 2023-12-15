WEB_APP_MESSAGE = Web app is running at http://localhost:8501/

# Dockerコンテナを起動してイメージをビルド
up-build:
	docker-compose up -d --build
	@echo "$(WEB_APP_MESSAGE)"

# Dockerコンテナを起動
up:
	docker-compose up -d
	@echo "$(WEB_APP_MESSAGE)"

# Dockerコンテナを修了
down:
	docker-compose down

# Qdrantのデータを検索
search-db: ## make search-db query="検索ワード"
	docker-compose exec web python /app/devtools/search_db.py "$(query)"

# QdrantのCollectionを削除
delete-db:
	docker-compose exec web python /app/devtools/delete_db.py
