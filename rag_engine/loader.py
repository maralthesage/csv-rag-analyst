import pandas as pd


def load_and_prepare_csv(csv_path: str) -> pd.DataFrame:
    df = pd.read_csv(
        csv_path,
        sep=";",
        encoding="cp850",
        ### Adapt this to your data and the columns it has
        usecols=['NUMMER', 'AUFTRAG_NR', 'RECHNUNG', 'Land', 'SOURCE', 'AUF_ANLAGE',
       'Herkunft', 'Brutto_Umsatz', 'Netto_Umsatz', 'Produkt', 'MENGE',
       'Retouren', 'WG_NAME'],
    )
    df["AUFTRAG_NR"] = df["AUFTRAG_NR"].astype(str).str.replace(".0", "", regex=False).str.zfill(9)
    df["NUMMER"] = df["NUMMER"].astype(str).str.zfill(10)
    df["AUF_ANLAGE"] = pd.to_datetime(df["AUF_ANLAGE"], errors="coerce")
    df = df.dropna(subset=["AUF_ANLAGE"])
    for col in ["Netto_Umsatz", "MENGE", "Brutto_Umsatz"]:
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

    for col in df.columns:
        if type(df[col]) == str:
            df[col] = df[col].fillna("")
        elif type(df[col]) == float:
            df[col] = df[col].fillna(0)
    return df
