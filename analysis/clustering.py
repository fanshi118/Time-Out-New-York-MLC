from sklearn.cluster import spectral_clustering
import numpy as np

s = np.matrix([[1, 2, 3, 4],
               [2, 1, 2, 5],
               [3, 2, 4, 2],
               [4, 5, 2, 3]])
labels = spectral_clustering(s, n_clusters=2, eigen_solver='arpack')
