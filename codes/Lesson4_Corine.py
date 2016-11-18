# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 09:08:58 2016

@author: hentenka
"""

import geopandas as gpd
import matplotlib.pyplot as plt


# Download datasets
# -----------------

# Download (and then extract) the data from this link: 

# Data preparation
# ----------------

# File path
fp = r"C:\HY-Data\HENTENKA\KOODIT\Opetus\Automating-GIS-processes\AutoGIS-Sphinx\data\Corine2012_Uusimaa.shp"
data = gpd.read_file(fp)

# Drop Finnish columns
selected_cols = ['Level1', 'Level1Eng', 'Level2', 'Level2Eng', 
       'Level3', 'Level3Eng', 'Luokka3', 'geometry']

# Select data
data = data[selected_cols]

# Check coordinate system information
data.crs

# Okey we can see that the units are in meters and we have a `UTM projection  <https://en.wikipedia.org/wiki/Universal_Transverse_Mercator_coordinate_system>`_

# Let's plot the data and use column 'Level3' as our color
data.plot(column='Level3', linewidth=0.05)

# Use tight layout and remove empty whitespace around our map
plt.tight_layout()

# Let's see what kind of values we have in 'Level3Eng' column
list(data['Level3Eng'].unique())

# Select lakes (i.e. 'waterbodies' in the data) and make a proper copy out of our data
lakes = data.ix[data['Level3Eng'] == 'Water bodies'].copy()
lakes.head()


# Calculations in DataFrames
# --------------------------


# Calculate the area of lakes
lakes['area'] = lakes.area

# The values are in square meters so let's change those into square kilometers 
lakes['area_km2'] = lakes['area'] / 1000000

# What is the mean size of our lakes?
l_mean_size = lakes['area_km2'].mean()
l_mean_size

# Okey so the size of our lakes seem to be approximately 1.58 square kilometers 

# Classifying data
# ----------------

# Let's classify our data into small and large lakes where the dividing limit (threshold) that we use is the average size of the lake
# First we need to create a function for our classification task

def binaryClassifier(row, source_col, output_col, threshold):
    # If area of input geometry is lower that the threshold value
    if row[source_col] < threshold:
        # Update the output column with value 0
        row[output_col] = 0
    # If area of input geometry is higher than the threshold value update with value 1
    else:
        row[output_col] = 1
    # Return the updated row
    return row

# We can use our custom function by using a Pandas / Geopandas function called ``.apply()``
# Let's create an empty column for our classification
lakes['small_big'] = None

# Let's apply our function
lakes = lakes.apply(binaryClassifier, source_col='area_km2', output_col='small_big', threshold=l_mean_size, axis=1)

# Note: There is also a way of doing this without a function but it might be easier to understand how the function works and doing 
# more complicated criteria should definately be done in a function as it is much more human readable
# Let's give a value 0 for small lakes and value 1 for big lakes by using an alternative technique
lakes['small_big_alt'] = None
lakes.loc[lakes['area_km2'] < l_mean_size, 'small_big_alt'] = 0
lakes.loc[lakes['area_km2'] >= l_mean_size, 'small_big_alt'] = 1

# Let's plot these lakes and see how they look like
lakes.plot(column='small_big', linewidth=0.05, cmap="seismic")
plt.tight_layout()

# Okey so it looks like they are correctly classified

# Simplifying geometries
# ----------------------

# What I want to do next is to only include the big lakes and simplify them slightly so that they are not as detailed

# Let's take only big lakes
big_lakes = lakes.ix[lakes['small_big'] == 1].copy()

# Let's see how they look
big_lakes.plot(linewidth=0.05, color='blue')
plt.tight_layout()

# The Polygons that are presented there are quite detailed, let's generalize them a bit

# Generalization can be done easily by using a Shapely function called ``.simplify()``. The ``tolerance`` parameter is adjusts how much
# geometries should be generalized. **The tolerance value is tied to the coordinate system of the geometries**. 
# Thus, here the value we pass is 250 **meters**.
big_lakes['geom_gen'] = big_lakes.simplify(tolerance=250)

# Let's set the geometry to be our new column
big_lakes['geometry'] = big_lakes['geom_gen']

# Let's see how they look now
big_lakes.plot(linewidth=0.05, color='blue')
plt.tight_layout()

# Great! Now we can see that our Polygons have been simplified a bit that are good for visualizing larger areas

# Classifying based on multiple criteria
# --------------------------------------

# Let's modify our binaryClassifier function a bit so that it classifies the data based on two columns
# Let's call it customClassifier2 as it takes into account two criteria

def customClassifier2(row, src_col1, src_col2, threshold1, threshold2, output_col):
    # If area of input geometry is lower that the threshold value
    if row[src_col1] < threshold1:
        # Update the output column with value 0
        row[output_col] = 0
    # If area of input geometry is higher than the threshold value update with value 1
    else:
        row[output_col] = 1
    # Return the updated row
    return row


