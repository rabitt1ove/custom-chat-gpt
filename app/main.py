import streamlit as st
from client.qdrant_manager import QdrantManager
from modules.url_scraping import URLScraping
from modules.ask_from_scraped_data import AskFromScrapedData

def init_page():
    """
    アプリケーションの初期UI設定を行います。
    タイトル、アイコン、サイドバーなどの基本的な設定を含みます。
    """

    # アプリケーションのUI設定
    st.set_page_config(page_title="URL Scraping and Embedding", page_icon="📖")
    st.sidebar.title("Options")

    # セッション状態の初期化
    if "emb_model_name" not in st.session_state:
        st.session_state.emb_model_name = "gpt-3.5-turbo"
    if "messages" not in st.session_state:
        st. session_state.messages = []
    if "costs" not in st.session_state:
        st.session_state.costs = []

def handle_page_selection(qdrant_manager):
    """
    ユーザーのページ選択に応じて適切なページの内容を表示します。
    サイドバーでの選択に基づいてページを表示します。
    """

    # サイドバーでのページ選択処理
    selection = st.sidebar.radio("Go to", ["Scrape and Build DB", "Ask From Scraped Data"])

    # 選択に応じたページの表示
    if selection == "Scrape and Build DB":
         url_scraping = URLScraping(qdrant_manager)
         url_scraping.scrape_url_and_build_db()
    elif selection == "Ask From Scraped Data":
        ask_from_scraped_data = AskFromScrapedData(qdrant_manager)
        ask_from_scraped_data.page_ask_from_scraped_data()

def main():
    """
    アプリケーションのメイン関数です。
    UIの初期化、依存関係の設定、ページ選択のハンドリングを行います。
    """

    # ページの初期化
    init_page()
    
    # ページ選択の処理
    handle_page_selection(QdrantManager())

if __name__ == '__main__':
    main()
