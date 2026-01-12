import numpy as np
A = np.array([[2, -2, 3], [1, 1, 1], [1, 3, -1]])
print(A)

#calculate eigenpairs: 
values, vectors = np.linalg.eig(A)
print(values)
print(vectors)
