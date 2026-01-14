#define the dataset:
import numpy as np
import matplotlib.pyplot as plt
X = np.array([[0, 1, 2, 3, 4, 5, 1, 2, 3, 3, 5, 6, 7, 8], [1, 2, 3, 3, 5, 5, 0, 1, 1, 2, 3, 5, 6, 6]])

y = np.array([0,0,0,0,0,0,1,1,1,1,1,1,1,1])
X = X.T
plt.scatter(X[:,0], X[:, 1], c = y)

#Apply PCA: 

from sklearn.decomposition import PCA
pca = PCA(n_components = 1)
pca.fit(X)
Xr = pca.transform(X)
print(Xr)

plt.scatter(Xr[: ,0], Xr[:,0], c = y)
