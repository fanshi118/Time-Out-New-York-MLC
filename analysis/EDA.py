import pandas as pd
df = pd.read_csv('../data/cleanMessage.csv')
partDf = df[['user_id', 'time', 'venue_id', 'venue_name', 'venue_category']]
# print partDf['user_id'].value_counts()
venues = partDf.apply(lambda row: partDf.groupby(
    'user_id').get_group(row['user_id'])['venue_name'].tolist(), axis=1)
print 'Groupby finished'
partDf.to_csv('../data/result.csv', index=False)
