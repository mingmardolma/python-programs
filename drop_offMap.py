#This program that asks the user for the name of a CSV file, 
#name of the output file, the name of a borough and 
#creates a map with markers for all the textile drop-off locations 
#in that borough from the input file.

import folium
import pandas as pd

in_file = input("Please enter the name of the input file:")
out_file = input("Please enter the name of the ouput file:")
borough = input("Please enter the name of the borough:")

tt_dropoff_nyc = pd.read_csv(in_file)
borough_nyc = tt_dropoff_nyc.groupby('Borough').get_group(borough)

map = folium.Map(location=[0,0])

for index,row in borough_nyc.iterrows():
	lat = row["Latitde"]
	lon = row["Longitude"]
	name = row["Address"]
	newMarker = folium.Marker([lat, lon], popup=name)
	newMarker.add_to(map)

map.save(outfile = out_file)