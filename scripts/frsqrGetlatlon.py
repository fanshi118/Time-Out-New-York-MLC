import csv
import glob
from frsqrRequests import VenueSearch
import pandas as pd

# Get Full Latlon

# fullLatlon = open('../data/fullLatlon.csv', 'wb')
# w = csv.writer(fullLatlon)
# w.writerow(['lat', 'lon'])
# lat_lon = []
# for data in glob.glob("../data/*output/part*"):
#     f = open(data, 'rb')
#     csv_reader = csv.reader(f)
#     for record in csv_reader:
#         if (record[-3] != 'null') and (record[-2] != 'null'):
#             lat_lon.append((float(record[-3]), float(record[-2])))
# lat_lon = set(lat_lon)
# for i in lat_lon:
#     w.writerow(i)


# myfile = open('../data/fullVenuelist_18.csv', 'wb')
# wr = csv.writer(myfile)
# wr.writerow(['venue_id', 'venue_name', 'veunue_category'])
# l = pd.read_csv('../data/fullLatlon.csv')
# k = 2
# for idx, val in l.iterrows():
# After each round of 1500 venue search, change credentials
# k = 4 - (idx // 1500 % 5)
#     if idx >= 118124:
#         k = (1 + idx // 1500) % 5
#         print k, idx, val[0], val[1]
#         row = VenueSearch(val[0], val[1], k)
#         print [s.encode('utf-8') for s in row]
#         wr.writerow([s.encode('utf-8') for s in row])

# Merge data
fout = open("../Data/fullVenuelist.csv", 'wb')
fout.write("venue_id, venue_name, veunue_category\n")
for data in glob.glob("../data/fullVenuelist_*"):
    f = open(data, 'rb')
    f.next()
    for line in f:
        fout.write(line)
    f.close()
fout.close()
