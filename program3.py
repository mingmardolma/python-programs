"""
Name: Mingmar Dolma
Email: Mingmar.Dolma17@myhunter.cuny.edu
Date: August 28, 2021
This program prints selects rows where the field senate_class is non-empty and write the first_name 
and compute the age based on the birthday field as of the first of the year. 
Your program should write out a new CSV file (with the name provided by the user) with the two columns: first_name and age.
Resources: used csci 127 to review python
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


