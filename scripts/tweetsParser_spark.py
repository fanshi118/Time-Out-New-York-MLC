__author__="Shi Fan"
from pyspark.sql import SQLContext
from pyspark.sql.types import *
from datetime import datetime
import json

def load_data_as_json(tweets):
	for twit in tweets:
		try:
			yield json.loads(twit)
		except:
			pass

sqlContext = SQLContext(sc)
tweets = sc.textFile("PATH_TO_THE_INPUT_FILE")
tweets_json = tweets.mapPartitions(load_data_as_json)

foursquares = tweets_json.filter(lambda t: 'foursquare.com' in t['source'])
foursquares = foursquares.filter(lambda f: f['place'] != None)
foursquares_red = foursquares.map(lambda f: (f['user']['id_str'], f['user']['name'], f['user']['description'], f['lang'], f['text'], f['created_at'].replace("+0000 ", ""), f['geo']['coordinates'][0], f['geo']['coordinates'][1], f['place']['full_name']))
features = ['user_id','user_name','user_descr','language','tweet_text','tweet_time','lat','lon','city']

fields = [StructField(feature, StringType(), True) for feature in features]
fields[-4].dataType = TimestampType()
fields[-3].dataType = FloatType()
fields[-2].dataType = FloatType()
schema = StructType(fields)

foursquares_temp = foursquares_red.map(lambda p: (p[0], p[1], p[2], p[3], p[4], datetime.strptime(str(p[-4]),'%a %b %d %H:%M:%S %Y'), p[-3], p[-2], p[-1]))
foursquares_df = sqlContext.createDataFrame(foursquares_temp, schema)
foursquares_df.write.format("com.databricks.spark.csv").save("PATH_TO_THE_OUTPUT_FILE")