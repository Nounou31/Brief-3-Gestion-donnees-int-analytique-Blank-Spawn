import pandas as pd

def load_raw_data():
    operations = pd.read_csv("data/operations.csv")
    flotteurs = pd.read_csv("data/flotteurs.csv")
    resultats = pd.read_csv("data/resultats_humain.csv")
    return operations, flotteurs, resultats

def clean_operations(df):

    return df

def clean_flotteurs(df):

    return df

def clean_resultats(df):

    return df

def save_clean_data(ops, flot, res):
    ops.to_csv("data/operations_clean.csv", index=False)
    flot.to_csv("data/flotteurs_clean.csv", index=False)
    res.to_csv("data/resultats_humain_clean.csv", index=False)

if __name__ == "__main__":
    ops, flot, res = load_raw_data()
    ops = clean_operations(ops)
    flot = clean_flotteurs(flot)
    res = clean_resultats(res)
    save_clean_data(ops, flot, res)
