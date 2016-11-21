# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 09:25:56 2016
@author: root

"""
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# read in data
jumbo = "/home/geo/dataE4/TravelTimes_to_5878070_Jumbo.txt"
itis = "/home/geo/dataE4/TravelTimes_to_5944003_Itis.txt"
Forum = "/home/geo/dataE4/TravelTimes_to_5975373_Forum.txt"


grid_fp = "/home/geo/dataE4/MetropAccess_YKR_grid_EurefFIN.shp"

border_fp = "/home/geo/data/Helsinki_borders.shp"
hel = gpd.read_file(border_fp)

# Read files
grid = gpd.read_file(grid_fp)

# Read in the text files
jumbo =  pd.read_csv(jumbo, sep=";")
itis =  pd.read_csv(itis, sep=";")
Forum =  pd.read_csv(Forum, sep=";")



jumbo = jumbo.rename(columns={'pt_r_tt':'pt_r_tt_jumbo'})
jumbo.columns.values

itis = itis.rename(columns={'pt_r_tt':'pt_r_tt_itis'})
jumbo.columns.values

Forum = Forum.rename(columns={'pt_r_tt':'pt_r_tt_Forum'})


#check columns
Jumbo.columns.values
grid.columns.values

# List of columns to select
columns = ['from_id', 'to_id','pt_r_tt', 'car_r_t']

# Select Listed columns
Jumbo = Jumbo[columns]

grid_Jumbo = grid.merge(Jumbo, left_on='YKR_ID', right_on='from_id')



#iterate over the accessibility files one by one




#rename the travel time columns so that they can be identified

#you can include e.g. the to_id number as part of the column name (then the column name could be e.g. "pt_r_tt_5987221")

#Join those columns into MetropAccess_YKR_grid_EurefFIN.shp where YKR_ID in the grid corresponds to from_id in the travel time data file. At the end you should have a GeoDataFrame with different columns show the travel times to different shopping centers.

#For each row find out the minimum value of all pt_r_tt_XXXXXX columns and insert that value into a new column called min_time_pt. You can now also parse the to_id value from the column name (i.e. parse the last number-series from the column text) that had the minimum travel time value and insert that value as a number into a column called dominant_service. In this, way are able to determine the "closest" shopping center for each grid cell and visualize it either by travel times or by using the YKR_ID number of the shopping center (i.e. that number series that was used in column name).
#



#Visualize the travel times of our min_time_pt column using a common classifier from pysal (you can choose which one).

#Visualize also the values in dominant_service column (no need to use any specific classifier). Notice that the value should be a number. If it is still as text, you need to convert it first.

#Upload the map(s) you have visualized into your own Exercise 4 repository (they don't need to be pretty)