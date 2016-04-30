from __future__ import division
import pandas as pd
import numpy as np
import userSimilarity as sim
import tqdm


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
    print df[df['user_id']==userid]
    print visitedVenueName
    predict = pd.read_csv('../data/result/covCosSimilar.csv')
    userPredict = (predict.iloc[user, :])
    userPredict.sort(axis=1, ascending=False)
    print userPredict[:30]
    predictIndex = [int(i) for i in userPredict[:50].index]
    print uniqueVenue.loc[predictIndex]
# checkIn()

# recommend()
# np.random.seed(430)
np.random.seed(666)
userid = np.random.randint(4365)
print userid
recommend(userid)
