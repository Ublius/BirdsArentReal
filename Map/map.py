import geopandas as gpd
import matplotlib.pyplot as plt

# Load the US states shapefile
gdf = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
us_states = gdf[gdf['continent'] == 'North America']

# Plot the map
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
us_states.boundary.plot(ax=ax)
plt.title("Map of the United States")
plt.show()