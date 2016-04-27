import tweepy, glob, csv
from settings import *
auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

#u = api.get_user(id=404203580)
def getTwitterIDs(ids=[]):
	for data in glob.glob("../data/*output/part*"):
		f = open(data, 'r')
		csv_reader = csv.reader(f)
		for record in csv_reader:
			ids.append(record[0])
	return list(set(ids))