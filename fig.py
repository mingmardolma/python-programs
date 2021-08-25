"""
This program asks the user for the name of the borough and name of the output file.
this program will output the min, max, average, median, and standard deviation (std) of the population of the borogh entered by user 
and then displayes the fraction of population that has lived in that borough overtime.
"""

import matplotlib.pyplot as plt
import pandas as pd

borough = input("Enter borough name: ")
outputName = input("Enter output name:")

pop = pd.read_csv('nycHistPop.csv', skiprows= 5)

print("Min: ", pop[borough].min())
print("Max: ", pop[borough].max())
print("Mean: ", pop[borough].mean())
print("Median: ", pop[borough].median())
print("Standard Deviation: ", pop[borough].std())

pop["Fraction"] = pop[borough] / pop["Total"]
pop.plot(x = "Year", y = "Fraction")

fig = plt.gcf()

fig.savefig(outputName)