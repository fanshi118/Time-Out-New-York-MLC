import csv
# from frsqr import getLatLons
from frsqrRequests import VenueSearch
import pandas as pd

myfile = open('../data/venueList.csv', 'wb')
wr = csv.writer(myfile)
wr.writerow(['lat', 'lon'])
l = pd.read_csv('../data/latlon.csv')
for idx, val in l.iterrows():
    # After each round of 1500 venue search, change credentials
    k = idx // 1500 % 3
    print idx
    row = VenueSearch(val[0], val[1], k)
    print [s.encode('utf-8') for s in row]
    wr.writerow([s.encode('utf-8') for s in row])
