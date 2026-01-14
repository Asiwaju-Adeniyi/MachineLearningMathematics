import numpy as np
import matplotlib.pyplot as plt

X = np.array([[1, 3, 5, 7, 9, 13, 20, 20, 21, 24, 26],[5, 7, 11, 14, 15, 17, 18, 19, 21, 22, 26]])
X = X.T
print(X)

plt.scatter(X[:,0], X[:,1])
X_meaned = X - np.mean(X, axis=0)
print(X_meaned)
plt.figure
plt.scatter(X_meaned[:, 0], X_meaned[:,1])
plt.scatter(X[:,0], X[:,1])
C = np.cov(X_meaned, rowvar=False)
print(C)

eval, evec = np.linalg.eig(C)
print(eval)
print(evec)

sorted_index = np.argsort(eval)[::-1]
sorted_eval=eval[sorted_index]
sorted_evec = evec[:, sorted_index]

n = 1
evec_subset = sorted_evec[:, 0:n]
print(evec_subset)
