__author__='Shi Fan'
import urllib2, json
import pandas as pd, numpy as np

if __name__ == '__main__':
	tweets = pd.read_csv('../data/tweets_parsed.csv')
	lat_lon = [(tweets.loc[i,'lat'], tweets.loc[i,'lon']) for i in np.arange(0,len(tweets))]

	# https://developer.foursquare.com/docs/explore#req=venues/
	token = YOUR_TEMPORARY_ACCESS_TOKEN
	venues = []
	for i in lat_lon:
		url = 'https://api.foursquare.com/v2/venues/search?ll=%.8f,%.8f%s'%(i[0],i[1],token)
		request = urllib2.urlopen(url)
		venue = json.load(request)
		try:
			venues.append((venue['response']['venues'][0]['name'],venue['response']['venues'][0]['categories'][0]['name']))
		except:
			venues.append(('None','None'))

	tweets['venue_name'] = [i[0] for i in venues]
	tweets['venue_type'] = [i[1] for i in venues]
	tweets.to_csv('../data/tweets_merged.csv', encoding='utf-8', index=False)