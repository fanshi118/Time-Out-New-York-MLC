from __future__ import division
import pandas as pd
import sklearn.preprocessing as pp
import scipy.sparse as sp
import numpy as np
import scipy.io as sio
import json
from getSomething import getUsers, convertUnicodeToInt


cosMatrix_mat = sio.loadmat(
    '../data/result/cosMatrix.mat', struct_as_record=False,
    squeeze_me=True)['cosMatrix']

similarityCosSum = pd.DataFrame(
    cosMatrix_mat.sum(axis=1)) - cosMatrix_mat.diagonal().reshape(4365, 1)

checkin = pd.read_csv('../data/result/checkinMatrix.csv')

users = getUsers()

with open('../data/twitter_user_network.json') as jsonFile:
    userNetwork = json.load(jsonFile)

userNetwork = convertUnicodeToInt(userNetwork)
userNetwork_mat = np.ndarray(shape=cosMatrix_mat.shape, dtype=np.int64)
for row, i in enumerate(users):
    if i in userNetwork.keys():
        for friend in userNetwork[i]:
            friend_idx = np.where(users == friend)[0][0]
            userNetwork_mat[row][friend_idx] = 1

userNetwork_mat = sp.csr_matrix(userNetwork_mat)
sio.savemat('../data/result/userFriends.mat', {'userFriends': userNetwork_mat})
