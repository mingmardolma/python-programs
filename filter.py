"""
selective
"""

import pandas as pd
import numpy as np

infile = input("Enter input file name: ")
outfile = input("Enter output file name: ")

df = pd.read_csv(infile)

df = df.loc[(df["Grade"] == 3) & (df["Year"] == 2019)]
df.index.names = [" "]
df.to_csv(outfile)

