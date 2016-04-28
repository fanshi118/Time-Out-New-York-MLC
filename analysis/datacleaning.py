import csv
import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim
import geopy
geolocator = Nominatim()

# Part 1: Read unique (lat,lon) from merged_message.csv and write uniqueLoc.csv
# df = pd.read_csv('../data/merged_message.csv',
#                  dtype={'user_id': str, 'lon': str, 'venue_idx': str})
# loc = []
# for i, row in df.iterrows():
#     loc.append("{},{}".format(row['lat'], row['lon']))
# uniqueLoc = list(set(loc))
# myfile = open('../data/uniqueLoc.csv', 'wb')
# wr = csv.writer(myfile)
# for i in uniqueLoc:
#     wr.writerow([i])

# uniqueLoc = pd.read_csv('../data/uniqueLoc.csv', header=None)
# counties = open('../data/partCounty.csv', 'a')
# w = csv.writer(counties)
# for i, loc in uniqueLoc.iterrows():
#     if i >= 1034:
#         print i
#         try:
#             print loc[0]
#             location = geolocator.reverse(loc[0])
#             city = location.raw['address']['county']
#             print city
#             w.writerow([loc[0], city])
#         except geopy.exc.GeocoderServiceError:
#             print loc[0]
#             print 0
#             w.writerow([loc[0], 0])

# Part 2: Some geopy quest failed, read those with 0 value in county and redo.
# partCounty = pd.read_csv('../data/partCounty.csv', 'wb', delimiter=",")
# while len(partCounty[partCounty['county'] == '0']) > 0:
#     print len(partCounty[partCounty['county'] == '0'])
#     for i, row in partCounty.iterrows():
#         if row['county'] == '0':
#             try:
#                 location = geolocator.reverse(
#                     "{},{}".format(row['lat'], row['lon']))
#                 county = location.raw['address']['county']
#                 partCounty.iloc[i, 2] = county
#                 print partCounty.iloc[i, :].values
#             except geopy.exc.GeocoderServiceError:
#                 print row.value
# partCounty.to_csv('../data/partCounty.csv', index=False)

# Part 3: Add Label 1 for in city 0 for out of city
county = pd.read_csv('../data/partCounty.csv')
county.loc[:, 'label'] = np.zeros(len(county))
for i, row in county.iterrows():
    if county.iloc[i, 2] in ['Kings County', 'Queens County',
                             'New York County', 'Bronx County']:
        county.iloc[i, 3] = 1
county.to_csv('../data/venueCounty.csv', index=False)
print county.head()
