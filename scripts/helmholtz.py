import random

from scipy import sparse
from scipy.sparse import linalg
# from numpy import linalg
import numpy as np

# Generate the matrix of the one dimensional discrete Poisson equation on N grid points
# N: grid points 
# The matrix is returned in CRS format
def generate_1D_matrix(h):
    N = int(1 / h - 1)
    assert(N > 1),"N > 1 required"
    a = sparse.diags([2 / h**2] * N, 0, format="csr")
    b = sparse.diags([-1 / h**2] * (N-1), 1, format="csr")
    c = sparse.diags([-1 / h**2] * (N-1), -1, format="csr")
    A = a + b + c
    # To convert to a numpy array
    # A = A.toarray();
    return A


# Generate the matrix of the two dimensional discrete Poisson equation on a square grid
# N + 2: dimension of the grid 
# The matrix is returned in CRS format
def generate_2D_matrix(h, k):
    N = int(1 / h - 1)
    assert(N > 1),"N > 1 required"
    B = generate_1D_matrix(h)
    I = sparse.eye(N)
    A = sparse.kron(B, I) + sparse.kron(I, B) - sparse.diags([(k * h)**2]*N*N, 0, format="csr")
    # To convert to a numpy array
    # A = A.toarray()
    return A

x = []
y = []
for i in range(0, 6):
    k = 5 * 2**i
    h = 0.625 / k
    N = 1/h - 1
    A = generate_2D_matrix(h, k)
    res1 = linalg.eigsh(A, which='LM')
    res2 = linalg.eigsh(A, which='SM')
    ew1 = np.abs(res1[0])
    ew2 = np.abs(res2[0])
    cond = np.max(ew1) / np.min(ew2)
    x.append(k)
    y.append(cond)
    print("k: ", k, "cond(A):", cond)

import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rc
import matplotlib.font_manager as font_manager

rc('text', usetex=True)
sns.set(style="white")
sns.set_context("paper")
sns.set_style('ticks', {'font.family': 'serif', 'font.serif': 'Times New Roman'})

ax = sns.lineplot(x=x, y=y, marker="s")
# plt.xscale('log')
# plt.yscale('log')
plt.xlabel("k")
plt.ylabel("Condition Number")
ax.set_xlim(0, 165)
plt.tight_layout()
plt.savefig("cond.pdf")
