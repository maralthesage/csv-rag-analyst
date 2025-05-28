
import streamlit as st
from rag_engine.loader import load_and_prepare_csv
from rag_engine.analyzer import OllamaCsvRAG
from config import rechnung_path

# ✅ Title
st.title("📊 CSV RAG Chatbot (Ollama-based)")

# ✅ Load your CSV ONCE at app startup
@st.cache_resource
def load_rag():
    df = load_and_prepare_csv(rechnung_path)
    rag = OllamaCsvRAG(df)
    return rag

rag = load_rag()

st.success("RAG engine initialized and CSV loaded.")

# 📝 Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# ✅ Display previous chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ✅ Chat input
question = st.chat_input("Ask something about the CSV...")

if question:
    # Display user message
    with st.chat_message("user"):
        st.write(question)

    # Get answer from RAG
    answer = rag.ask(question)

    # Display assistant message
    with st.chat_message("assistant"):
        st.write(answer)

    # Streamlit session
    st.session_state.messages.append({"role": "user", "content": question})
    st.session_state.messages.append({"role": "assistant", "content": answer})
