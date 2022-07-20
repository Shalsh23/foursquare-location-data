from geopy.geocoders import Nominatim
import pandas as pd
import certifi
import ssl

ctx = ssl.create_default_context(cafile=certifi.where())
# geopy.geocoders.options.default_ssl_context = ctx

geolocator = Nominatim(user_agent="kaggle-foursquare", ssl_context=ctx)

# poi = pd.read_csv('/Users/shalkishrivastava/renci/Learning/kaggle/foursquare-location-matching/train.csv')

Latitude = "25.594095"
Longitude = "85.137566"

location = geolocator.reverse(Latitude+","+Longitude)
print(location.raw)

