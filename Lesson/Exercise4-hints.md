# Exercise 4: Hints

Documentation of the Travel Time Matrix dataset and explanation for different column names can be found at the Accessibility Research Group website: [http://blogs.helsinki.fi/accessibility/helsinki-region-travel-time-matrix-2015/] (
http://blogs.helsinki.fi/accessibility/helsinki-region-travel-time-matrix-2015/)

### Problem 1:
- Note that the input travel time data is stored in text files when reading in the data.
- *Correction to instructions*: keep columns `'from_id'`,`'to_id'`,`'pt_r_tt'` and `'car_r_t'` in the travel time data files
- Join the data using columns `'from_id'` from the travel time data, and `'YKR_ID'` in the grid-shapefile
- See hints for joining the travel time data to the grid shapefile from **Lesson 3 materials: [Table join] (https://automating-gis-processes.github.io/2016/Lesson3-table-join.html#table-join)**
- IF the overlay-operation does not go trough in a decent amount of time you can skip this step and move on to visualizing travel times for the whole grid (plotting the map also takes a while).

### Problem 2:



