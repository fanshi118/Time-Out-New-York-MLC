import json
import csv
__author__ = 'Shi Fan'


def parse(foursquares):
    with open('../data/tweets_parsed.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([
            'tweet_text',
            'tweet_time',
            'lat',
            'lon',
            'city',
            'language',
            'user_id',
            'user_name',
            'user_descr'
        ])

        for i in foursquares:
            tweet_text = i['text'].encode('utf-8')
            tweet_time = i['created_at']
            lat = i['geo']['coordinates'][0]
            lon = i['geo']['coordinates'][1]
            city = i['place']['full_name']
            language = i['lang']
            user_id = i['user']['id_str']
            user_name = i['user']['name'].encode('utf-8')
            try:
                user_descr = i['user']['description'].encode('utf-8')
            except AttributeError:
                user_descr = 'None'.encode('utf-8')

            writer.writerow([
                tweet_text,
                tweet_time,
                lat,
                lon,
                city,
                language,
                user_id,
                user_name,
                user_descr
            ])

if __name__ == '__main__':
    data = []
    with open('../data/twitter_jsons_sample.txt', 'r') as f:
        for line in f:
            data.append(json.loads(line))

    foursquares = [i for i in data if 'foursquare.com' in i['source']]
    parse(foursquares)
