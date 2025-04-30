import pandas as pd


def load_and_prepare_csv(csv_path: str) -> pd.DataFrame:
    df = pd.read_csv(
        csv_path,
        sep=";",
        encoding="cp850",
        usecols=[
            "AUFTRAG_NR",
            "WG_NAME",
            "PREIS",
            "MWST",
            "MENGE",
            "MEDIACODE",
            "BEZEICHNG",
            "AUF_ANLAGE",
            "NUMMER",
            "ART_NR",
        ],
    )
    df["AUFTRAG_NR"] = df["AUFTRAG_NR"].astype(str).str.replace(".0", "", regex=False)
    df["NUMMER"] = df["NUMMER"].astype(str)
    df["AUF_ANLAGE"] = pd.to_datetime(df["AUF_ANLAGE"], errors="coerce")
    df = df.dropna(subset=["AUF_ANLAGE"])
    for col in ["PREIS", "MENGE", "MWST"]:
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)
    for col in df.columns:
        if type(df[col]) == str:
            df[col] = df[col].fillna("")
        elif type(df[col]) == float:
            df[col] = df[col].fillna(0)
    return df
