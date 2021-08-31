"""
Name: Mingmar Dolma
Email: Mingmar.Dolma17@myhunter.cuny.edu
Date: August 28, 2021
This program select rows where the field Grade is equal to 3 and the Year is equal to 2019 and 
write all rows that match that criteria to a new CSV file.
Resources: used csci 127 to review python
"""

import pandas as pd
import numpy as np

infile = input("Enter input file name: ")
outfile = input("Enter output file name: ")

df = pd.read_csv(infile)

df = df.loc[(df["Grade"] == 3) & (df["Year"] == 2019)]
df.index.names = [" "]
df.to_csv(outfile)

