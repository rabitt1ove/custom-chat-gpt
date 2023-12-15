import streamlit as st
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.callbacks import get_openai_callback

class AskFromScrapedData:
    def __init__(self, qdrant_manager):
        self.qdrant_manager = qdrant_manager

    def page_ask_from_scraped_data(self):
        st.title("Ask From Scraped Data")

        self._display_chat_history()
        self.spinner_container = st.empty()

        llm = self._create_chat_model()
        st.text_input("Query: ", key="query_input", on_change=self._handle_query, args=(llm,))

        self._handle_clear_button()
        self._display_costs()

    def _display_chat_history (self):
        st.markdown("""
            <style>
            .chat-message {
                word-wrap: break-word;
            }
            </style>
            """, unsafe_allow_html=True)

        if not st.session_state.get('messages'):
            return
        for message in st.session_state.messages:
            with st.chat_message(message['type']):
                 st.markdown(message['content'], unsafe_allow_html=False)

    def _create_chat_model(self):
        temperature = 0.1
        model_name = st.session_state.emb_model_name
        st.session_state.max_token = OpenAI.modelname_to_contextsize(model_name) - 200
        return ChatOpenAI(temperature=temperature, model_name=model_name)

    def _handle_query(self, llm):
        query = st.session_state.query_input
        if query:
            qa = self._build_qa_model(llm)
            if qa:
                with self.spinner_container:
                    with st.spinner("Processing ..."):
                        output, cost = self._ask(qa, query)
                        answer = output['result']
                    st.session_state.costs.append(cost)
                    st.session_state.messages.append({'type': 'user', 'content': query}) 
                    st.session_state.messages.append({'type': 'assistant', 'content': answer})
                    st.session_state.query_input = ""

    def _build_qa_model(self, llm):
        retriever = self.qdrant_manager.qdrantNLP.as_retriever(search_type="similarity", search_kwargs={"k": 10})
        return RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=retriever,
            return_source_documents=True,
            verbose=True
        )

    def _ask(self, qa, query):
        with get_openai_callback() as cb:
            answer = qa(query)
        return answer, cb.total_cost

    def _handle_clear_button(self):
        clear_button = st.sidebar.button("Clear Conversation", key="clear")
        if clear_button:
            st.session_state.messages = []
            st.experimental_rerun()

    def _display_costs(self):
        st.sidebar.markdown("## Costs")
        costs = st.session_state.get('costs', [])
        total_cost = sum(costs)
        last_cost = costs [-1] if costs else 0
        st.sidebar.markdown(f"**Total cost: ${total_cost:.5f}**")
        st.sidebar.markdown(f"**Last cost: ${last_cost:.5f}**")
