
from __future__ import division
import pandas as pd
import scipy.sparse as sp
import numpy as np
import scipy.io as sio
import json

def getUsers():
	df = pd.read_csv('../data/result/checkinsFinal.csv')
	return df['user_id'].unique()

def getVenues():
	df = pd.read_csv('../data/result/checkinsFinal.csv')
	return df['venue_id'].unique()

def convertUnicodeToInt(jsonFile={}):
	newFile = {}
	tempList = []
	for key,val in jsonFile.iteritems():
		for i in val:
			tempList.append(np.int64(i))
		newFile[np.int64(key)] = tempList
		tempList = []
	return newFile

def getUserMatrix():
	cosMatrix_mat = sio.loadmat(
		'../data/result/cosMatrix.mat', struct_as_record=False,
		squeeze_me=True)['cosMatrix']

	users = getUsers()

	with open('../data/twitter_user_network.json') as jsonFile:
		userNetwork = json.load(jsonFile)

	userNetwork = convertUnicodeToInt(userNetwork)
	userNetwork_mat = np.ndarray(shape=cosMatrix_mat.shape, dtype=np.int64)
	for row,i in enumerate(users):
		if i in userNetwork.keys():
			for friend in userNetwork[i]:
				friend_idx = np.where(users==friend)[0][0]
				userNetwork_mat[row][friend_idx] = 1
	userNetwork_mat = sp.csr_matrix(userNetwork_mat)
	return userNetwork_mat
	