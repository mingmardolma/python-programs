"""
Name: Mingmar Dolma
Email: Mingmar.Dolma17@myhunter.cuny.edu
Date: August 28, 2021
This program selects rows where the field senate_class is non-empty and write the first_name and last_name 
to a file with the output file name provided by the user.
Resources: used csci 127 to review python
"""
import pandas as pd
import numpy as np

infile_name = input("Enter input file name: ")
outfile_name = input("Enter output file name: ")
df = pd.read_csv(infile_name)

#updates same df file by removing rows with nan(not a number) values in specified column
df.dropna(subset = ["senate_class"], inplace=True)

# OR
# df = df[df["senate_class"].notna()] 
# OR
# df = df[df['senate_class'].notnull()]   <<selecting rows with non_empty senate_class
# all methods above gives same result
fullname = df[["first_name", "last_name"]] 
fullname.to_csv(outfile_name)
