import numpy as np
from sklearn.metrics import jaccard_similarity_score

def getJaccardSimilarity(user1=None, user2=None):
	if user1.ndim!=1 or user2.ndim!=1:
		print 'Input arrays must be 1-dimensional'
		return
	elif user1.shape!=user2.shape:
		print 'Input arrays must have the same length'
		return
	else:
		return jaccard_similarity_score(user1,user2)

def get_sim_index_based_on_freq(user1=None, user2=None, normalize=False):
	if user1.ndim!=1 or user2.ndim!=1:
		print 'Input arrays must be 1-dimensional'
		return
	elif user1.shape!=user2.shape:
		print 'Input arrays must have the same length'
		return
	else:
		if normalize:
			user1 = user1/float(np.sum(user1))
			user2 = user2/float(np.sum(user2))
		index_to_sum = np.intersect1d(np.nonzero(user1), np.nonzero(user2))
	return float(np.sum(user1[index_to_sum])+np.sum(user2[index_to_sum]))/2