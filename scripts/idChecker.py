import json
import numpy as np
from frsqrGettwitter import getIDsFromCleanData

def convertUnicodeToInt(jsonFile={}):
	newFile = {}
	tempList = []
	for key,val in jsonFile.iteritems():
		for i in val:
			tempList.append(np.int64(i))
		newFile[np.int64(key)] = tempList
		tempList = []
	return newFile

def main():
	with open("../data/twitter_following_scraped.json", "rb") as infile:
		followings = json.load(infile)

	allIDs = getIDsFromCleanData()

	followingsInt = convertUnicodeToInt(followings)

	userNetwork = {}
	for key,val in followingsInt.iteritems():
		network = list(np.intersect1d(np.array(val), allIDs))
		if network!=[]:
			userNetwork[key] = network

	with open("../data/twitter_user_network.json", "wb") as outfile:
		json.dump(userNetwork, outfile)

if __name__=="__main__":
	main()