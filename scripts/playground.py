import numpy as np

a = np.array([0, 1, 0])
b = np.reshape(a, (3,1))
c = np.array([[0,1,0],[1,4,1],[0,1,0]])
# c = np.kron(a,b)
d = np.kron(a, c)
print(d)
