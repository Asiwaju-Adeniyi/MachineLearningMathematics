import numpy as np

v = np.array([1, -1, 2])
w = np.array([2, 5, 2])

print(v + w)
print(v - w)

#Scalar Mult:
print(3 * v)

print(np.linalg.norm(v))
s=np.dot(v,w)
print(s)
