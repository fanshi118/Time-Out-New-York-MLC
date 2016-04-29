import pandas as pd
df = pd.read_csv('../data/cleanMessage.csv')

partDf = df[['user_id', 'time', 'venue_id', 'venue_name', 'venue_category']]
uniqueVenue = partDf['venue_id'].unique()
uniqueUser = partDf['user_id'].unique()
checkin = pd.DataFrame(0, index=uniqueUser, columns=uniqueVenue)
for user in uniqueUser:
    print len(partDf[partDf['user_id'] == user])
