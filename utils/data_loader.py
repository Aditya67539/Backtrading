import pandas as pd

def load_csv(path: str):
    df = pd.read_csv(path)

    # Data cleaning
    df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
    df = df.sort_values("Date")
    df["Price"] = df["Price"].str.replace(",", "").astype(float)

    return df