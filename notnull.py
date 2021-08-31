"""
This program selects rows where the field senate_class is non-empty and write the first_name and last_name 
to a file with the output file name provided by the user.
"""
import pandas as pd
import numpy as np

infile_name = input("Enter input file name: ")
outfile_name = input("Enter output file name: ")
df = pd.read_csv(infile_name)

df.dropna(subset = ["senate_class"], inplace=True)
fullname = df[["first_name", "last_name"]] 
fullname.to_csv(outfile_name)
