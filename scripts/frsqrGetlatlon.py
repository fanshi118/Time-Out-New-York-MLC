#!/usr/bin/env python
# __author__ = "Yuxiang Zhang"
# -*- coding: utf-8 -*-
import csv
import glob
from frsqrRequests import VenueSearch
import pandas as pd
import time
import numpy as np

# Part 1: Get Full Latlon
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

# Part 2:
#     Quest API for venue information
# myfile = open('../data/fullVenuelist.csv', 'a')
# wr = csv.writer(myfile)
# wr.writerow(['venue_id', 'venue_name', 'veunue_category'])
# l = pd.read_csv('../data/fullLatlon.csv')
# for idx, val in l.iterrows():
# After each round of 1500 venue search, change credentials
#     if idx >= 128749:
#         if (idx % 9000 == 1):
#             time.sleep(500)
#         k = (idx // 1500) % 6
#         print k, idx, val[0], val[1]
#         row = VenueSearch(val[0], val[1], k)

#         row[:0] = [str(idx)]
#         wr.writerow([s.encode('utf-8') for s in row])

# Part 3: Merge data
# Merge with fullLatlon.csv
# fLatlon = open("../data/fullLatlon.csv", "rb")
# csvLatlon = csv.reader(fLatlon)
# loc = []
# for record in csvLatlon:
#     loc.append((record[0], record[1]))
# fVenue = open("../data/fullVenuelist.csv")
# csvVenue = csv.reader(fVenue)
# venue = []
# for record in csvVenue:
#     venue.append(record)
# mergedVenue = np.hstack([loc, venue])
# venue_df = pd.DataFrame(mergedVenue)
# venue_df.columns = venue_df.iloc[0]
# venue_df = venue_df.reindex(venue_df.index.drop(0))
# venue_df.to_csv('../data/mergedVenue.csv',index=False)
venue_df = pd.read_csv('../data/mergedVenue.csv', low_memory=False)
message_df = pd.read_csv("../data/fullOutput.csv", low_memory=False)
# merged_df = pd.merge(message_df, venue_df, on=['lat', 'lon'])
# merged_df.to_csv('../data/merged_message.csv', index=False)
print venue_df.head()