# from flask import Flask, request, render_template
# from rag_engine.loader import load_and_prepare_csv
# from rag_engine.analyzer import OllamaCsvRAG

# app = Flask(__name__)
# df = load_and_prepare_csv("/Volumes/MARAL/rechnung/rechnung_F04.csv")
# rag = OllamaCsvRAG(df)

# @app.route("/", methods=["GET", "POST"])
# def home():
#     answer = ""
#     if request.method == "POST":
#         question = request.form["question"]
#         answer = rag.ask(question)
#     return render_template("index.html", answer=answer)

# if __name__ == "__main__":
#     app.run(debug=True)
import streamlit as st
from rag_engine.loader import load_and_prepare_csv
from rag_engine.analyzer import OllamaCsvRAG

# ✅ Title
st.title("📊 CSV RAG Chatbot (Ollama-based)")

# ✅ Load your CSV ONCE at app startup
@st.cache_resource
def load_rag():
    df = load_and_prepare_csv("/Users/maralsheikhzadeh/Documents/Codes/Repeating-Analytics/rechnung-preparing-for-rag/rechnung_gesamt.csv")
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

    # Save to history
    st.session_state.messages.append({"role": "user", "content": question})
    st.session_state.messages.append({"role": "assistant", "content": answer})
