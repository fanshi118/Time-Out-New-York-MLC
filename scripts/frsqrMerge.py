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
# message = [['use_id', 'username', 'description', 'lan',
#             'message', 'time', 'lat', 'lon', 'city']]
fout = open("../data/fullOutput.csv", 'wb')
wr = csv.writer(fout)
wr.writerow([
    'use_id', 'username', 'description', 'lan', 'message', 'time', 'lat', 'lon', 'city'])
for data in glob.glob("../data/*_output/part*"):
    f = open(data, 'r')
    csv_reader = csv.reader(f)
    for record in csv_reader:
        wr.writerow(record)

# message_df = pd.DataFrame(message)
# message_df.columns = message_df.iloc[0]
# message_df = message_df.reindex(message_df.index.drop(0))
# venue_df = pd.DataFrame(merged)
# venue_df.columns = venue_df.iloc[0]
# venue_df = venue_df.reindex(venue_df.index.drop(0))
# merged_df = pd.merge(message_df, venue_df, on=['lat', 'lon'])
# merged_df.to_csv('../data/merged_message.csv', index=False)
