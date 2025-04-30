from flask import Flask, request, render_template
from rag_engine.loader import load_and_prepare_csv
from rag_engine.analyzer import OllamaCsvRAG

app = Flask(__name__)
df = load_and_prepare_csv("/Volumes/MARAL/rechnung/rechnung_F04.csv")
rag = OllamaCsvRAG(df)

@app.route("/", methods=["GET", "POST"])
def home():
    answer = ""
    if request.method == "POST":
        question = request.form["question"]
        answer = rag.ask(question)
    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
