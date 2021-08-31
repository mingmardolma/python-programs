"""
age calculator
"""
import pandas as pd
import numpy as np
import datetime
infile = input("Enter input file name: ")
outfile = input("Enter output file name: ")

df = pd.read_csv(infile)

df.dropna(subset=["senate_class"], inplace=True)

df["birthday"] = pd.to_datetime(df["birthday"].apply(str))
df["age"] = ((datetime.datetime(2021,1,1) - df["birthday"]).astype("<m8[Y]")).astype(int)
df2 = df[["first_name", "age"]]

df2.to_csv(outfile)


