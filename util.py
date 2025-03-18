from random import randint

import numpy as np
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

def summarise_cnf(cnf):
    accuracy = np.diagonal(cnf).sum() / cnf.sum()
    print(f"Accuracy: {accuracy}")
    precision = cnf[1, 1] / cnf[:, 1].sum()
    print(f"Precision: {precision}")
    sensitivity = cnf[1, 1] / cnf[1].sum()
    print(f"Sensitivity: {sensitivity}")
    specificity = cnf[0, 0] / cnf[0].sum()
    print(f"Specificity: {specificity}")
    print(cnf)

def rand_seed():
    return randint(0, 1000)