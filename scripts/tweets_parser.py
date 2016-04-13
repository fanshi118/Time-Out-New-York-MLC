__author__='Shi Fan'
import json, csv

if __name__ == '__main__':
	data = []
	with open('../input/twitter_jsons_sample.txt','r') as f:
		for cnt,line in enumerate(f):
			data.append(json.loads(line))
		f.close()

	with_urls = [i for i in data if i['entities']['urls']!=[]]
	foursquares = [i for i in with_urls if 'foursquare.com' in i['source']]
	
	with open('../data/tweets_parsed.csv', 'wb') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow([
			'tweet_text',
			'lat',
			'lon',
			'city',
			'user_id',
			'user_name',
			'user_descr'
			])

		for i in foursquares:
			tweet_text = i['text'].encode('utf-8')
			lat = i['geo']['coordinates'][0]
			lon = i['geo']['coordinates'][1]
			city = i['place']['full_name'].encode('utf-8')
			user_id = i['user']['id_str'].encode('utf-8')
			user_name = i['user']['name'].encode('utf-8')
			try:
				user_descr = i['user']['description'].encode('utf-8')
			except AttributeError:
				user_descr = 'None'.encode('utf-8')

			row = [
				tweet_text,
				lat,
				lon,
				city,
				user_id,
				user_name,
				user_descr
				]

			writer.writerow(row)

		csvfile.close()