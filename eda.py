# import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

poi = pd.read_csv('/Users/shalkishrivastava/renci/Learning/kaggle/foursquare-location-matching/train.csv', dtype='object')
# poi.head(2)
# print(poi.columns)

# which filed values are null?
na_col = poi.isnull()
# print(na_col.head(5))

# number of NaN values in each field
na_sum = na_col.sum()
# print(type(na_sum))

# print("number of samples: ", len(na_col))

# %age of NaN in each field
# print(na_sum.values / len(poi) * 100)

# print(na_sum.index)
# print(na_sum.axes)
# print(na_sum.columns)
# print(na_sum.values)

na_plt = na_sum[na_sum.values > len(poi) * 0.2]
# print(type(na_plt))
# print(na_plt)
# print(na_sum[na_sum.values < len(poi) * 0.2])
# print(na_sum.values)
# print(len(poi)*0.2)

# plt.figure(figsize=(20,4))
# na_plt.plot(kind='bar')
# plt.title('columns list and NA values count more than 20%')
# plt.show()

lat = poi['latitude']
lng = poi['longitude']

# lat = pd.Series([1,2,3])
# lng = pd.Series([2,3,4])
# print(type(lat))
# plt.scatter(lat, lng)
# plt.show()
