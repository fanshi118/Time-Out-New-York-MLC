#!/usr/bin/env python
# __author__ = "Yuxiang Zhang"
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import glob
import csv

# fLatlon = open("../data/fullLatlon.csv", "rb")
# csvLatlon = csv.reader(fLatlon)
# loc = []
# for record in csvLatlon:
#     loc.append((record[0], record[1]))
# fVenue = open("../data/venueList.csv")
# csvVenue = csv.reader(fVenue)
# venue = []
# for record in csvVenue:
#     venue.append(record)
# merged = np.hstack([loc, venue])
# fout = open("../data/fullOutput.csv", 'wb')
# wr = csv.writer(fout)
# wr.writerow([
#     'use_id', 'message', 'time', 'lat', 'lon', 'city'])
# for data in glob.glob("../data/*_output/part*"):
#     f = open(data, 'r')
#     csv_reader = csv.reader(f)
#     for record in csv_reader:
#         row = record
#         row[1:] = row[4:]
#         wr.writerow(row)
venue_df = pd.read_csv('../data/mergedVenue.csv',
                       dtype={'lat': np.float64, 'lon': np.float64}, low_memory=False)
message_df = pd.read_csv(
    '../data/fullOutput.csv', dtype={'lat': np.float64, 'lon': np.float64}, low_memory=False)
print message_df.dtypes
print venue_df.dtypes
merged_df = pd.merge(message_df, venue_df, on=['lat', 'lon'])
merged_df.to_csv('../data/merged_message.csv', index=False)
