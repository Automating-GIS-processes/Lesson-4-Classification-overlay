# Exercise 4: Hints

Documentation of the Travel Time Matrix dataset and explanation for different column names can be found at the Accessibility Research Group website: [http://blogs.helsinki.fi/accessibility/helsinki-region-travel-time-matrix-2015/] (
http://blogs.helsinki.fi/accessibility/helsinki-region-travel-time-matrix-2015/)

### Problem 1:
- Note that the input travel time data is stored in text files when reading in the data.
- Keep columns `'from_id'`,`'to_id'`,`'pt_r_tt'` and `'car_r_t'` in the travel time data files
- Join the data using columns `'from_id'` from the travel time data, and `'YKR_ID'` in the grid-shapefile
- See hints for joining the travel time data to the grid shapefile from **Lesson 3 materials: [Table join] (https://automating-gis-processes.github.io/2016/Lesson3-table-join.html#table-join)**
- Plotting the data takes a while (be patient!)

### Problem 2:

#### Finding out which shopping center is the closest

We can find out the minimum value from multiple columns simply by applying a `.min()` function to those columns of a row that we are interessted in:

```
# Define the columns that are used in the query
value_columns = ['center1', 'center2', 'center3']

# Find out the minimum value of those column of a given row in the DataFrame
minimum_values = row[value_columns].min()
```

It is also possible to find out which column contains that value by applying [`.idxmin()`](http://pandas.pydata.org/pandas-docs/version/0.18.1/generated/pandas.DataFrame.idxmin.html) -function:

```
# Find out which column has the contains the minimum value
minimum_values = row[value_columns].idxmin()
```

