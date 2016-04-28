#!/usr/bin/env python
# __author__ = "Yuxiang Zhang"
# -*- coding: utf-8 -*-

import pandas as pd
from scipy.spatial.distance import cosine
data = pd.read_csv('../data/test/lastfm-matrix-germany.csv')
data_germany = data.drop('user', 1)
# Create a placeholder dataframe listing item vs. item
data_ibs = pd.DataFrame(
    index=data_germany.columns, columns=data_germany.columns)
# Lets fill in those empty spaces with cosine similarities
# Loop through the columns
for i in range(0, len(data_ibs.columns)):
    # Loop through the columns for each column
    for j in range(0, len(data_ibs.columns)):
        # Fill in placeholder with cosine similarities
        data_ibs.ix[i, j] = 1 - \
            cosine(data_germany.ix[:, i], data_germany.ix[:, j])
# Create a placeholder items for closes neighbours to an item
data_neighbours = pd.DataFrame(index=data_ibs.columns, columns=range(1, 11))

# Loop through our similarity dataframe and fill in neighbouring item names
for i in range(0, len(data_ibs.columns)):
    data_neighbours.ix[i, :10] = data_ibs.ix[
        0:, i].order(ascending=False)[:10].index

# --- End Item Based Recommendations --- #
