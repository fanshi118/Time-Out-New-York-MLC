from __future__ import division
import numpy as np
from sklearn.metrics import jaccard_similarity_score
from scipy.spatial.distance import cosine


def getJaccardSimilarity(user1=None, user2=None):
    if user1.ndim != 1 or user2.ndim != 1:
        print 'Input arrays must be 1-dimensional'
        return
    elif user1.shape != user2.shape:
        print 'Input arrays must have the same length'
        return
    else:
        return jaccard_similarity_score(user1, user2)


def getFrequencySimilarity(user1=None, user2=None, normalize=False):
    if user1.ndim != 1 or user2.ndim != 1:
        print 'Input arrays must be 1-dimensional'
        return
    elif user1.shape != user2.shape:
        print 'Input arrays must have the same length'
        return
    else:
        if normalize:
            user1 = user1 / np.sum(user1)
            user2 = user2 / np.sum(user2)
        index_to_sum = np.intersect1d(np.nonzero(user1), np.nonzero(user2))
    return (np.sum(user1[index_to_sum]) + np.sum(user2[index_to_sum])) / 2


def getCosineSimilarity(user1=None, user2=None):
    if user1.ndim != 1 or user2.ndim != 1:
        print 'Input arrays must be 1-dimensional'
        return
    elif user1.shape != user2.shape:
        print 'Input arrays must have the same length'
        return
    else:
        return 1-cosine(user1, user2)

# test cases below
# user1 = np.array([0, 1, 1, 3, 4, 2, 1])
# user2 = np.array([3, 1, 3, 4, 1, 4, 3])
# print getJaccardSimilarity(user1, user2)
# print getFrequencySimilarity(user1, user2, normalize=True)
# print getCosineSimilarity(user1, user2)
