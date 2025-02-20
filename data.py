import numpy as np
import pandas as pd

PATH = "data/root.xlsx"
SHEET = "Data"

# read
df = pd.read_excel(PATH, SHEET)
df.columns = [
    "nhs_num",
    "lab_num",
    "age",
    "gender",
    "location",
    "location_other",
    "size",
    "mdm2",
    "karyo_code",
    "diagnosis",
    "diagnosis_other",
    "follow_up",
    "mortality",
    "cancer_mortality",
    "comment",
    "query",
    "misc"
]

# CLEAN
# age todo
df.loc[df["age"] == "\xa0", "age"] = np.nan
# gender
df["gender"] = df["gender"].str.lower()
df.loc[df["gender"] == "\xa0", "gender"] = np.nan
# location
df.loc[df["location"] == "\xa0", "location"] = np.nan
nnans = df.loc[~df["location"].isna(), "location"]
df.loc[~df["location"].isna(), "location"] = nnans.apply(lambda x: x.split("-")[0].lower().strip())
# location other
# size
df.loc[df["size"] == "\xa0", "size"] = np.nan
# mdm2
df["mdm2"] = df["mdm2"].str.lower().str.lower()
df.loc[df["mdm2"] == "\xa0", "mdm2"] = np.nan
df.loc[df["mdm2"] == "non-amplified", "mdm2"] = 0
df.loc[df["mdm2"] == "amplified", "mdm2"] = 1
# karyo code
df["karyo_code"] = df["karyo_code"].str.lower()
# diagnosis
df["diagnosis"] = df["diagnosis"].str.strip().str.lower()
df.loc[df["diagnosis"] == "\xa0", "diagnosis"] = np.nan
# diagnosis other
df["diagnosis_other"] = df["diagnosis_other"].str.strip().str.lower()
# follow up
# mortality
df["mortality"] = df["mortality"].str.strip().str.lower()
df.loc[df["mortality"] == "\xa0", "mortality"] = np.nan
nnans = df.loc[~df["mortality"].isna(), "mortality"]
df.loc[~df["mortality"].isna(), "mortality"] = nnans.apply(lambda x: -1 if x == "alive" else int(x.split()[1]))
# cancer mortality
df.loc[df["cancer_mortality"] == "\xa0", "cancer_mortality"] = np.nan
# comment
# query
# misc

mask = df["diagnosis"].str.contains("lipoma") | \
    df["diagnosis"].str.contains("liposarcoma") | \
    df["diagnosis_other"].str.contains("lipoma") | \
    df["diagnosis_other"].str.contains("liposarcoma")
    
# age size and location

df.to_csv("out.csv",)