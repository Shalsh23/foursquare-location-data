import pandas as pd
import certifi
import ssl

from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
# import tqdm
# from tqdm._tqdm_notebook import tqdm_notebook
# from shapely.geometry import Point
# import geopandas as gpd

poi = pd.read_csv('/Users/shalkishrivastava/renci/Learning/kaggle/foursquare-location-matching/train.csv')
# for development, use test.csv or test_mini.csv
# poi = pd.read_csv('/Users/shalkishrivastava/renci/Learning/kaggle/foursquare-location-matching/test.csv')

# setup
ctx = ssl.create_default_context(cafile=certifi.where())
# geopy.geocoders.options.default_ssl_context = ctx
geolocator = Nominatim(user_agent="kaggle-foursquare", ssl_context=ctx)

## example - usage of geolocator.reverse()
# Latitude = "25.594095"
# Longitude = "85.137566"
# location = geolocator.reverse(Latitude+","+Longitude)
# print(location.raw)

## example - concat 2 columns
# poi["coordinates"] = poi["longitude"].map(str) + ',' + poi["latitude"].map(str)
# print(poi["coordinates"][0])
# geometry = [Point(xy) for xy in zip(poi["longitude"], poi["latitude"])]

## example - working with GeoDataFrame
# crs = {'init': 'EPSG:4326'}
# geo_df = gpd.GeoDataFrame(poi, crs = crs, geometry = geometry)
# print(geo_df.head())

# tqdm.pandas() #fixme - library to display progress

def reverse_geolocator(row):
    coordinates = str(row['latitude']) + "," + str(row['longitude'])
    return geolocator.reverse(coordinates).raw

limiter = RateLimiter(reverse_geolocator, min_delay_seconds=0.001)
poi['address'] = poi.apply(limiter, axis=1)

# print(poi['address'].values)


