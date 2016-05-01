from __future__ import division
import pandas as pd
import numpy as np

from getSomething import getFriendsMatrix
import scipy.io as sio
from sklearn.cluster import spectral_clustering


def checkIn():
    df = pd.read_csv('../data/result/checkinsFinal.csv')
    partDf = df[
        ['user_id', 'time', 'venue_id', 'venue_name', 'venue_category']]
    uniqueVenue = partDf['venue_id'].unique()
    uniqueUser = partDf['user_id'].unique()
    checkin = pd.DataFrame(0, index=uniqueUser, columns=uniqueVenue)
    for i, user in enumerate(uniqueUser):
        for j, venue in enumerate(partDf[partDf['user_id'] == user]['venue_id']):
            checkin[venue][user] += 1
        print "{}%".format(i / float(len(uniqueUser)))
    checkin.to_csv('../data/result/checkinMatrix.csv', index=False)


def recommend(user):
    df = pd.read_csv('../data/result/checkinsFinal.csv')
    partDf = df.drop_duplicates(cols='venue_id')
    uniqueVenue = partDf[
        ['venue_id', 'venue_name', 'venue_category']].reset_index(drop=True)
    # print uniqueVenue.head()
    uniqueUser = list(df['user_id'].unique())
    userid = uniqueUser[user]
    visitedVenueID = df[df['user_id'] == userid]['venue_id']
    visitedVenueName = uniqueVenue[uniqueVenue.venue_id.isin(visitedVenueID)]
    print visitedVenueName
    predict = pd.read_csv('../data/result/covCosSimilar.csv')
    userPredict = (predict.iloc[user, :])
    userPredict.sort(axis=1, ascending=False)
    print userPredict[:30]
    predictIndex = [int(i) for i in userPredict[:50].index]
    print uniqueVenue.loc[predictIndex]


def combinedRecommend(user):
    df = pd.read_csv('../data/result/checkinsFinal.csv')
    partDf = df.drop_duplicates(cols='venue_id')
    uniqueVenue = partDf[
        ['venue_id', 'venue_name', 'venue_category']].reset_index(drop=True)
    uniqueUser = list(df['user_id'].unique())
    userid = uniqueUser[user]
    visitedVenueID = df[df['user_id'] == userid]['venue_id']
    visitedVenueName = uniqueVenue[uniqueVenue.venue_id.isin(visitedVenueID)]
    print visitedVenueName
    combinedPredict = pd.read_csv('../data/result/combinedPredict.csv')
    userPredict = combinedPredict.iloc[user, :]
    userPredict.sort(axis=1, ascending=False)
    print userPredict[:30]
    predictIndex = [int(i) for i in userPredict[:50].index]
    print uniqueVenue.loc[predictIndex]


def clusterSimilarity(matrix, labels, c):
    clustDict = {}
    for i in range(c):
        clustDict[i] = [j for j, x in enumerate(labels) if x == i]

    averageClusterSim = 0
    for key, value in clustDict.iteritems():
        w = 0
        for p in value:
            for q in value:
                if p != q:
                    w += matrix[p, q]
        w /= len(value)
        averageClusterSim += w
    averageClusterSim /= c
    return averageClusterSim


def clustering():
    cosMatrix_mat = sio.loadmat(
        '../data/result/cosMatrix.mat', struct_as_record=False,
        squeeze_me=True)['cosMatrix']
    userMatrix_mat = getFriendsMatrix()
    combinedMatrix_mat = userMatrix_mat + cosMatrix_mat
    clusterNumber = range(50,60)
    sims = []
    for c in clusterNumber:
        labels = spectral_clustering(
            combinedMatrix_mat, n_clusters=c, eigen_solver='arpack')
        sim = clusterSimilarity(combinedMatrix_mat, labels, c)
        sims.append(sim)
        print "{} cluster: average simi={}".format(c, sim)
    print sims
# Part 1: Get check-in matrix
# checkIn()
# Part 2: Get memory-based recommendation
# recommend()
# Example 1 seed
np.random.seed(430)
# Example 2 seed
# np.random.seed(666)
userid = np.random.randint(4365)
# print userid
# recommend(userid)

# Part 3: Get trust-based
# combinedRecommend(userid)
# clustering()
userMatrix = getFriendsMatrix()
print userMatrix[userid]