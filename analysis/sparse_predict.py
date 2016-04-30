from __future__ import division
import pandas as pd
import sklearn.preprocessing as pp
import scipy.sparse as sp
import numpy as np
import scipy.io as sio

df = pd.read_csv('../data/result/checkinsFinal.csv')
partDf = df[
    ['user_id', 'time', 'venue_id', 'venue_name', 'venue_category']]
uniqueVenue = partDf['venue_id'].unique()
uniqueUser = partDf['user_id'].unique()


def cosine_similarities(mat):
    col_normed_mat = pp.normalize(mat.tocsc(), axis=0)
    return col_normed_mat.T * col_normed_mat

print("Calculate cosine similarity matrix.....")
checkin = pd.read_csv('../data/result/checkinMatrix.csv')
checkin_T = checkin.T
mat = sp.csr_matrix(checkin_T)
cosMatrix = cosine_similarities(mat)
# print cosMatrix
sio.savemat('../data/result/cosMatrix.mat', {'cosMatrix': cosMatrix})
cosMatrix_mat = sio.loadmat(
    '../data/result/cosMatrix.mat', struct_as_record=False,
    squeeze_me=True)['cosMatrix']
# print cosMatrix_mat
# Shape(4365, 4365)


print("Predicting similarity based on cosMatrix")
cosPredict = pd.DataFrame(
    0, index=range(len(uniqueUser)), columns=range(len(uniqueVenue)))
similarityCosSum = pd.DataFrame(
    cosMatrix_mat.sum(axis=1)) - cosMatrix.diagonal().reshape(4365, 1)
# print similarityCosSum
# d = pd.DataFrame([[i for j in range(838)]
#                   for i in similarityCosSum.iloc[:, 0]])
# Shape(4365,1)
covCosSimilar = pd.DataFrame(cosMatrix_mat * checkin)
covCosSimilar.to_csv('../data/result/covCosSimilar.csv', index=False)
print covCosSimilar
# Shape(4365, 838)

# for i, row in covCosSimilar.iterrows():
#     if i < 838:
#         covCosSimilar[i] = covCosSimilar[i] / similarityCosSum.iloc[i, 0]
# cosPredict.to_csv('../data/result/cosPredict.csv', index=False)
