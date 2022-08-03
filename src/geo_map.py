"""
- plot location data on map
- uses geopandas library
- shapefile: https://www.naturalearthdata.com/downloads/50m-cultural-vectors/

references:
- https://www.youtube.com/watch?v=HnWNhyxyUHg&ab_channel=MiddleburyRemoteSensing
- https://www.youtube.com/watch?v=PICwxT0fTHQ&ab_channel=EsriEvents
- https://geopandas.org/en/stable/docs/user_guide/projections.html
- https://towardsdatascience.com/plotting-maps-with-geopandas-428c97295a73
- https://towardsdatascience.com/geopandas-101-plot-any-data-with-a-latitude-and-longitude-on-a-map-98e01944b972

"""


import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Point


world_map = gpd.read_file('/Users/shalkishrivastava/renci/Learning/kaggle/foursquare-location-matching/ne_50m_admin_0_countries/ne_50m_admin_0_countries.shp')

fig, ax = plt.subplots(figsize=(5,15))
# world_map.plot(ax = ax)
# plt.show()

poi = pd.read_csv('/Users/shalkishrivastava/renci/Learning/kaggle/foursquare-location-matching/train.csv')

poi_samples = poi.head(10000)
# # print(poi_samples.head())
# # print(poi_samples.columns)
# # print(poi_samples.dtypes)
# crs = {'init': 'EPSG:4326'}
#
# geometry = [Point(xy) for xy in zip(poi_samples["longitude"], poi_samples["latitude"])]
# geo_df = gpd.GeoDataFrame(poi_samples, crs = crs, geometry = geometry)
# # print(geo_df.head())
# fig, ax = plt.subplots(figsize = (15, 15))
# world_map.to_crs(epsg=4326).plot(ax = ax, alpha = 0.3, color = "grey")
# geo_df.plot(ax = ax)
# ax.set_title('foursqaure location data')
# plt.show()


crs = {'init': 'EPSG:4326'}

geometry = [Point(xy) for xy in zip(poi["longitude"], poi["latitude"])]
geo_df = gpd.GeoDataFrame(poi, crs = crs, geometry = geometry)
fig, ax = plt.subplots(figsize = (15, 15))
world_map.to_crs(epsg=4326).plot(ax = ax, alpha = 0.3, color = "grey")
# geo_df.plot(ax = ax, alpha = 0.1, markersize = 0.5)
# ax.set_title('foursqaure location data')
# plt.savefig('foursquare location data map')
# plt.show()

# ----------------------------------------------------------------------------------------------------------------------
# try plotly library

import plotly.express as px

plotly_fig = px.scatter_mapbox(pd.DataFrame(poi.head(100)), lat="latitude", lon="longitude", zoom=15)
# print(plotly_fig)
# plotly_fig.show() # not working