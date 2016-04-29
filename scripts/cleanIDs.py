import pandas as pd, numpy as np

checkins = pd.read_csv("../data/cleanMessage.csv")

# drop venue categories that aren't related to local recreation
categories_to_drop = [
						'Airport', 
						'Bus Stop', 
						'Bus Station', 
						'Train Station', 
						'Bridge', 
						"Doctor's Office", 
						'Border Crossing', 
						'Gas Station', 
						'Bank',
						'Church',
						'Residential Building (Apartment / Condo)',
						'Office',
						'Tech Startup',
						'Non-Profit',
						'Coworking Space',
						'Hostel',
						'Hotel',
					]

checkins_cut = checkins.loc[~checkins.venue_category.isin(categories_to_drop)]
# print checkins_cut.venue_category.unique()

ids = checkins_cut.user_id.value_counts().index
counts = checkins_cut.user_id.value_counts().values
# drop users who checked in less than 5 times
ids_to_keep = ids[np.where(counts>=5)].tolist()
checkins_cut2 = checkins_cut.loc[checkins_cut.user_id.isin(ids_to_keep)]
# print len(checkins), len(checkins_cut), len(checkins_cut2)
# print len(checkins.venue_id.unique()), len(checkins_cut.venue_id.unique()), len(checkins_cut2.venue_id.unique())
# print len(checkins.user_id.unique()), len(checkins_cut.user_id.unique()), len(checkins_cut2.user_id.unique())

checkins_cut2.to_csv("../data/checkinsFinal.csv", index=False)