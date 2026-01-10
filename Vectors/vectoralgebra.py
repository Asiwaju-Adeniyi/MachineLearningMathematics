import numpy as np
P = np.array([[1,7], [2, 1], [3, 2]])
print(P)

Q = np.array([[1,1],[1,-1],[1,0]])
print(Q)


C1 = np.subtract(P,Q)
print(C1)


R = np.array([[1,3,1],[1,0,1]])
print(R)

C2 = np.dot(P,R)
print(C2)

det = np.linalg.det(C2)

M = np.array([[1,-1],[2,3]])
print(np.linalg.inv(M))


