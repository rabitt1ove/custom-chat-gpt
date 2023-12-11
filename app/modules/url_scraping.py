import streamlit as st
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from langchain.text_splitter import RecursiveCharacterTextSplitter

class URLScraping:
    def __init__(self, qdrant_manager):
        self.qdrant_manager = qdrant_manager

    def scrape_url_and_build_db(self):
        st.title("URL Scraping and Embedding")
        url_text = self._get_url_text()
        if not url_text:
            return
        if st.button("SUBMIT"):
            with st.container():
                st.session_state.spinner = st.spinner("Processing URL ...")
                self._build_vector_store(url_text)
                st.session_state.spinner = None

    def _get_url_text(self):
        url = st.text_input("Enter URL here:", key="input")
        is_valid_url = self._validate_url(url)
        if not is_valid_url:
            st.write('Please input a valid URL')
            return None
        return self._scrape_url(url)

    def _validate_url(self, url):
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except ValueError:
            return False

    def _scrape_url(self, url):
        st.write(f"Scraping URL: {url}")
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        content = soup.find('main') or soup.find('article')
        return content.get_text(' ', strip=True) if content else soup.get_text(' ', strip=True)

    def _build_vector_store(self, url_text):
        text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
            model_name=st.session_state.emb_model_name,
            chunk_size=250,
            chunk_overlap=0
        )
        split_text = text_splitter.split_text(url_text)
        for text in split_text:
            st.write(f"Processing text: {text[:50]}...")
            self.qdrant_manager.qdrant.add_texts([text])
