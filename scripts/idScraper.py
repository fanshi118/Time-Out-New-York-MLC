import tweepy, json, time
from settings import *
import pandas as pd, numpy as np
from frsqrGettwitter import getIDsFromCleanData

auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

# users = getIDsFromCleanData()
usersToScrape = getIDsFromCleanData()

# with open('../data/twitter_following_scraped.json') as data_file:
# 	scraped_users = json.load(data_file)

# scrapedIDs = scraped_users.keys()

# usersToScrape = np.setdiff1d(users, scrapedIDs, assume_unique=True)
# print len(users), len(scrapedIDs), len(usersToScrape)

# usersToScrape = np.append(usersToScrape[:2], np.split(usersToScrape[2:], 6)[0])

friendsDict = {}

for cnt,i in enumerate(usersToScrape):
	try:
		friends = api.friends_ids(user_id=i)

	except tweepy.RateLimitError:
		print "RATE LIMIT EXCEEDED AT", cnt
		time.sleep(60*15)
		try:
			friends = api.friends_ids(user_id=i)
		except tweepy.TweepError:
			continue

	except tweepy.TweepError:
		continue

	friendsDict[i] = friends

with open('../data/twitter_following_scraped.json', 'w') as fp:
	json.dump(friendsDict, fp)