# CSV RAG Analyst

A lightweight, local Retrieval-Augmented Generation (RAG) system for querying structured CSV data using natural language questions — powered by [Ollama](https://ollama.com/) and open-source models like gemma3:27b.

## 🚀 Features

* Ask complex questions about your CSV data in **natural language** (English or German)
* Automatically generates and runs **executable pandas code**
* Handles filters, grouping, aggregation, sorting, and datetime operations
* Can be run as an **interactive Streamlit web app**
* Designed for **local, private environments** – no cloud API required
* Supports flexible scaling to new datasets and departments

## 📦 Project Structure

```
csv-rag-analyst/
├── app.py                  # Streamlit app entrypoint
├── rag_engine/
│   ├── analyzer.py         # Core logic: LLM prompting and pandas execution
│   ├── loader.py           # CSV loading and cleaning
│   ├── prompts.py          # Prompt templates for LLMs
├── templates/              # (optional – legacy Flask folder, can be removed)
│   └── index.html
├── requirements.txt        # Python dependencies
└── README.md
```

## 🧠 How It Works

1. User submits a question like:
   *"Wie viel Umsatz hatten wir im Februar 2025?"*
2. The system:

   * Extracts schema context from the CSV
   * Generates a pandas query using the local LLM (e.g. gemma3:27b)
   * Executes the query and formats the result

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
ollama run gemma3:27b
```

Or pull explicitly:

```bash
ollama pull gemma3:27b
```

### 3. Start the Streamlit app

```bash
streamlit run app.py
```

Then open `http://localhost:8501/` in your browser.

---

## 📂 Add Your Own CSV

Update the CSV path in `rag_engine/loader.py` to point to your own file (UTF-8 or CP850 encoded). Of course the column names and the table schema needs to be updated accordingly.

Alternatively, implement a file uploader in `app.py` to allow dynamic CSV upload (feature planned in roadmap).

---

## 🛡️ Security

* No external API calls are made
* Runs fully locally
* Your data never leaves your machine

---

## 📈 Roadmap

* [ ] Multi-user login
* [ ] Dynamic CSV file upload via web UI
* [ ] Role-based access to datasets
* [ ] Contextual memory per department
* [ ] Long-form explanations and visualizations


