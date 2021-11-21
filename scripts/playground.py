import numpy as np

a = np.array([1, 2, 1])
b = np.reshape(a, (3,1))
c = np.kron(a,b)
d = np.kron(a, c)
print(d)