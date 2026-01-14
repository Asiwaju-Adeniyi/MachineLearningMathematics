from sklearn.datasets import load_wine
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split

wine = load_wine()
X = np.array(wine.data)
y = np.array(wine.target)

print(X[1:5,:])
print(y)

#Applying PCA: 

from sklearn.decomposition import PCA
pca = PCA(n_components=2)
result = pca.fit(X)

Z = result.transform(X)
plt.scatter(Z[:,0], Z[:,1], c=y)

#Apply LDA 
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
lda = LinearDiscriminantAnalysis()

X_lda = lda.fit_transform(X,y)
plt.scatter(X_lda[:,0], X_lda[:,1], c = y)


xtrain, xtest, ytrain, ytest = train_test_split(X, y, test_size = 0.3)

yn = lda.predict(xtest)
print(ytest)
print(yn)
print(ytest - yn)
