import streamlit as st

from core.app.main import build_vector_store
from core.app.rag_chain import build_chain

st.set_page_config(
    page_title="RepoMind AI",
    page_icon="🤖",
    layout="wide",
)

st.title("🤖 RepoMind AI")
st.caption("Analyze GitHub repositories using Gemini + LangChain RAG")

# ---------------- Session State ---------------- #

if "chain" not in st.session_state:
    st.session_state.chain = None

if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- Repository ---------------- #

repo_url = st.text_input(
    "GitHub Repository URL",
    placeholder="https://github.com/user/repository"
)

if st.button("Analyze Repository"):

    if not repo_url:
        st.warning("Please enter a GitHub repository URL.")
        st.stop()

    with st.spinner("Cloning repository and building vector database..."):

        vector_db = build_vector_store(repo_url)

        st.session_state.chain = build_chain(vector_db)

    st.success("Repository indexed successfully!")

# ---------------- Chat ---------------- #

if st.session_state.chain:

    st.divider()

    st.subheader("💬 Chat with the Repository")

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    question = st.chat_input("Ask anything about the repository...")

    if question:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question,
            }
        )

        with st.chat_message("user"):
            st.markdown(question)

        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                answer = st.session_state.chain.invoke(question)

                st.markdown(answer)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer,
            }
        )