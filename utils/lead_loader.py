import pandas as pd

def load_leads(path):
    return pd.read_csv(path)

def save_emails(df, path):
    df.to_csv(path, index=False)