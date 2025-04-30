import re
import pandas as pd
import numpy as np
from langchain.chains import LLMChain
from langchain_community.llms import Ollama
from .prompts import get_analysis_prompt

class OllamaCsvRAG:
    def __init__(self, df: pd.DataFrame, model: str = "mistral:latest"):
        self.df = df
        self.llm = Ollama(model=model)
        self.data_description = self._generate_schema()
        self.query_chain = LLMChain(llm=self.llm, prompt=get_analysis_prompt())
        self.column_name_hints = {
        "AUFTRAG_NR": (
            "Order ID (Auftragsnummer) — A unique identifier for each customer order. "
            "Can be used to count total number of sales. Example: 63877537"
        ),
        "WG_NAME": (
            "Product category (Warengruppe) — Describes the product group. "
            "Can be grouped to analyze revenue by category."
        ),
        "PREIS": (
            "Price (Umsatz, revenue) — The value of each item in EUR. "
            "Summing this gives total revenue. Numeric. Example: 29.95"
        ),
        "MWST": (
            "Value-added tax (Mehrwertsteuer) — Tax rate or amount applied to the PREIS. "
            "Used to calculate total tax per item or order."
        ),
        "MENGE": (
            "Quantity — Number of units ordered for the item. "
            "Useful for aggregating total items sold."
        ),
        "MEDIACODE": (
            "Marketing media code — Tracks which campaign or source drove the order. "
            "Can be grouped to analyze campaign performance."
        ),
        "BEZEICHNG": (
            "Product description, Artikel Bezeschnung oder Beschreibung — Text label or name of the product. "
            "Can be used to find most popular or frequent items."
        ),
        "AUF_ANLAGE": (
            "Order creation date, order date — datetime column in format YYYY-MM-DD. "
            "Use `.dt.year == 2025` to filter by year. "
            "Use `.dt.to_period('M') == '2025-02'` for month-level filters like February 2025."
        ),
        "NUMMER": (
            "Customer ID — customer identifier. May not be unique across files."
        ),
        "ART_NR": (
            "Article number — product identifier. May be repeated if product was ordered multiple times."
        )
    }


    def _generate_schema(self) -> str:
        lines = []
        for col in self.df.columns:
            dtype = str(self.df[col].dtype)
            hint = self.column_name_hints.get(col, "")
            lines.append(f"- {col} (Type: {dtype}) — Synonyms: {hint}")
        return "\n".join(lines)

    def _extract_code(self, output: str) -> str:
        match = re.search(r"```python(.*?)```", output, re.DOTALL)
        if match:
            code = match.group(1).strip()
            return code if code.startswith("result") else "result = " + code
        return "result = None"

    def _run_code(self, code: str) -> str:
        try:
            local_vars = {"df": self.df.copy(), "pd": pd, "np": np}
            exec(code, local_vars)
            result = local_vars.get("result", "No result")
            return result.to_markdown(index=False) if isinstance(result, pd.DataFrame) else str(result)
        except Exception as e:
            return f"Execution Error: {e}"

    def ask(self, question: str) -> str:
        llm_output = self.query_chain.run({
            "question": question,
            "data_description": self.data_description
        })
        code = self._extract_code(llm_output)
        return self._run_code(code)
