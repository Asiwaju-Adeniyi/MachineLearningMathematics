import numpy as np
A = np.array([[2, 0, 0], [0, 1, 0], [0, 0, -1]])
print(A)

#calculate eigenpairs: 
values, vectors = np.linalg.eig(A)
print(values)
print(vectors)
