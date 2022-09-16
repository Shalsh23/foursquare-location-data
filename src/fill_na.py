import pandas as pd
import numpy as np
import certifi
import ssl

from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
# from ratelimiter import RateLimiter
# import tqdm
# from tqdm._tqdm_notebook import tqdm_notebook
# from shapely.geometry import Point
# import geopandas as gpd

# poi = pd.read_csv('/Users/shalkishrivastava/renci/Learning/kaggle/foursquare-location-matching/train.csv')
# for development, use test.csv or test_mini.csv
poi = pd.read_csv('/Users/shalkishrivastava/professional_development/foursquare-location-data/data/mini_train.csv')

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

# def reverse_geolocator(row):
#     coordinates = str(row['latitude']) + "," + str(row['longitude'])
#     reverse = geolocator.reverse(coordinates) #.raw
#     print(coordinates)
#     return reverse

limit_geocode = RateLimiter(geolocator.reverse, min_delay_seconds = 1, return_value_on_exception = None)
print("****")
print(type(limit_geocode))


# limiter = RateLimiter(min_delay_seconds=0.1)
poi['address'] = np.nan
# print(poi)

# @RateLimiter(reverse_geolocator, min_delay_seconds=0.1)

for row in range(poi.shape[0]):
    # with limiter:
    # poi.at[row, 'address'] = reverse_geolocator(poi.iloc[row])
    coordinates = (poi.iloc[row]['latitude'], poi.iloc[row]['longitude'])
    coordinates = str(poi.iloc[row]['latitude']) + "," + str(poi.iloc[row]['longitude'])
    # print(poi.iloc[row]['address'])
    address = limit_geocode(coordinates).address
    address_split = address.split(", ")
    street_address = address_split[0]
    city_address = address_split[1]
    print(street_address, city_address)
    # poi.iloc[row]['address'] = limit_geocode(coordinates).address
    # print(type(limit_geocode(coordinates).address))
    # print(poi.iloc[row]['address'])
    break

# poi['address'] = poi.apply(limiter, axis=1)
# print(poi['address'].values)
# poi.to_csv("poi_address.csv", encoding='utf-8', index=False)


