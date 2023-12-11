# カスタムChatGPT
このカスタムChatGPT（AI Webアプリケーション）は、<br>
Webサイトからテキストをスクレイピングし、そのデータをベクトルDBに格納します。<br>
その後、カスタムChatGPTはベクトルDBのデータを活用して質問に回答できるようになります。<br>
例えば、以下のような使い方ができます。

## 使用例
- **個人的な知識ベース：**<br>
  特定のトピックや興味のある分野に関する情報を収集し、後で質問することができます。

- **学習目的での利用：**<br>
  教育関連のWebサイトやオンラインコースから情報を収集し、学習内容に関する質問に答えるためのリソースとして使用できます。

- **市場調査とデータ分析：**<br>
  複数のニュースサイトや業界レポートからデータを収集し、特定の市場トレンドや競合分析に関する質問に答えることができます。

## デモンストレーション
### スクレイビイングの結果
<img width="1624" alt="url_scraping" src="https://github.com/rabitt1ove/custom-chat-gpt/assets/45308877/6e5b8bb4-888f-4211-b764-723b837eaf33">

### 質問回答の結果
<img width="1624" alt="ask_from_scraped_data" src="https://github.com/rabitt1ove/custom-chat-gpt/assets/45308877/91bd95a9-acdf-46f6-89be-c4175eb28279">

## 要件
- Docker Desktop
- OpenAI API Key を発行

## インストール手順
1. **設定ファイルを作成：**<br>
   プロジェクトのルートディレクトリに `.env` ファイルを作成し、以下のようにOpenAI API Keyを定義します。
   ```env
   OPENAI_API_KEY=[YOUR-OPEN-AI-KEY]
   ```

2. **プロジェクトのビルドとDockerコンテナを起動：**<br>
   以下のコマンドを実行してプロジェクトをビルドし、Dockerコンテナを起動します。
   ```zsh
   make up-build
   ```

3. **アプリケーションを起動：**<br>
   Dockerコンテナが正常に起動したら、Webブラウザで http://localhost:8501/ にアクセスします。

## 使用方法
1. **スクレイビングとベクトルDBへの保存:**<br>
   サイドバーの `Scrape and Build DB` を選択した状態で<br>
   アプリケーションにURLを入力し、「SUBMIT」ボタンを押すことでスクレイピングが実行され。<br>
   結果がベクトルDBに保存されます。

2. **質問の方法:**<br>
   サイドバーの `Ask From Scraped Data` を選択した状態で<br>
   アプリケーションに質問内容を入力し、エンターキーを押すことで回答結果が画面に表示されます。

## 注意事項
- URLのスクレイピングはWebサイトの構造に依存します
