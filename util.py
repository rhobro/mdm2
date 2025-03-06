import pandas as pd

PATH = "data/clean.csv"

def load_with_columns(cols=None):
    # read
    sheet = pd.read_csv(PATH)

    # select columns
    if cols is None:
        cols = sheet.columns
    sheet = sheet[cols]

    # keep full rows
    rows_before = sheet.shape[0]
    sheet.dropna(inplace=True, ignore_index=True)
    rows_after = sheet.shape[0]

    print(f"Datapoints: {rows_before} --> {rows_after} ({rows_before - rows_after} removed)")
    return sheet[cols]