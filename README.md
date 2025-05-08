
# CSV RAG Analyst

A lightweight, local Retrieval-Augmented Generation (RAG) system for querying structured CSV data using natural language questions — powered by [Ollama](https://ollama.com/) and open-source models like Mistral.

## 🚀 Features

- Ask complex questions about your CSV data in **natural language** (English or German)
- Automatically generates and runs **executable pandas code**
- Handles filters, grouping, aggregation, sorting, and datetime operations
- Can be run as an **interactive Flask web app**
- Designed for **local, private environments** – no cloud API required
- Supports flexible scaling to new datasets and departments

## 📦 Project Structure

```
csv-rag-analyst/
├── app.py                  # Flask app entrypoint
├── rag_engine/
│   ├── analyzer.py         # Core logic: LLM prompting and pandas execution
│   ├── loader.py           # CSV loading and cleaning
│   ├── prompts.py          # Prompt templates for LLMs
├── templates/
│   └── index.html          # Simple UI for the web app
├── requirements.txt        # Python dependencies
└── README.md
```

## 🧠 How It Works

1. User submits a question like:  
   _"Wie viel Umsatz hatten wir im Februar 2025?"_
2. The system:
   - Extracts schema context from the CSV
   - Generates a pandas query using the local LLM (e.g. Mistral)
   - Executes the query and formats the result

## 🖥️ Run Locally

### 1. Clone the repo and set up a virtual environment

```bash
git clone https://github.com/maralthesage/csv-rag-analyst.git
cd csv-rag-analyst
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 2. Make sure Ollama is installed and a model is pulled

```bash
ollama run mistral
```

Or pull explicitly:

```bash
ollama pull mistral
```

### 3. Start the web app

```bash
streamlit run app.py
```

Then open `http://localhost:8501/` in your browser.

---

## 📂 Add Your Own CSV

Replace the path in `loader.py` with your own CSV file (UTF-8 or CP850 encoded). Columns like `PREIS`, `MENGE`, `AUF_ANLAGE`, etc. will be used to infer and answer questions.

---

## 🛡️ Security

- No external API calls are made
- Runs fully locally
- Your data never leaves your machine

---

## 📈 Roadmap

- [ ] Multi-user login
- [ ] Upload CSV files dynamically
- [ ] Role-based access to datasets
- [ ] Contextual memory per department
- [ ] Long-form explanations and visualizations





