import numpy as np
from scipy import sparse
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rc
import matplotlib.font_manager as font_manager


# Generate the matrix of the one dimensional discrete Poisson equation on N grid points
# N: grid points
# The matrix is returned in CRS format
def generate_1D_matrix(N):
    assert(N > 1),"N > 1 required"
    a = sparse.diags([2] * N, 0, format="csr")
    b = sparse.diags([-1] * (N-1), 1, format="csr")
    c = sparse.diags([-1] * (N-1), -1, format="csr")
    A = a + b + c
    # To convert to a numpy array
    # A = A.toarray();
    return A


def jacobi(A: sparse.csr_matrix, x: np.array, b: np.array, omega=1.0):
    r = b - A * x
    d = A.diagonal()
    d_inv = 1.0/d
    x_new = x + omega * sparse.diags(d_inv) * r
    return x_new


def plot_error(e, filename):
    x = np.linspace(0, 1, n)
    y = e
    rc('text', usetex=True)
    sns.set(style="whitegrid")
    sns.set_context("paper")
    sns.despine()
    sns.relplot(x=x, y=y, kind='line', color="black", dashes=False, legend=False)
    plt.tight_layout()
    plt.xlim(0, 1)
    plt.ylim(-0.1, 1.1)
    # plt.xticks(x, "")
    # plt.yticks(y, "")
    plt.savefig(filename, dpi=300)


def generate_jacobi_plots(A, x, b, steps=100, omega=2.0/3.0, fname1="initial_error.pdf", fname2="final_error.pdf"):
    e = x - b
    plot_error(e, fname1)
    for i in range(1, steps + 1):
        x_new = jacobi(A, x, b, omega)
        x = x_new
    e = x - b
    plot_error(e, fname2)


n = 1024
omega = 2/3
A = generate_1D_matrix(n)
b = np.zeros(n)

# Case 1
k = 4
tmp1 = np.linspace(0, k*np.pi, n)
x1 = 0.5 * (np.sin(tmp1) + 1)
x = x1
generate_jacobi_plots(A, x, b, fname1="initial_error1.pdf", fname2="final_error1.pdf")

k = 8
tmp1 = np.linspace(0, k*np.pi, n)
x1 = 0.5 * (np.sin(tmp1) + 1)
x = x1
generate_jacobi_plots(A, x, b, fname1="initial_error2.pdf", fname2="final_error2.pdf")

k = 16
tmp1 = np.linspace(0, k*np.pi, n)
x1 = 0.5 * (np.sin(tmp1) + 1)
x = x1
generate_jacobi_plots(A, x, b, fname1="initial_error3.pdf", fname2="final_error3.pdf")


k = 32
tmp1 = np.linspace(0, k*np.pi, n)
x1 = 0.5 * (np.sin(tmp1) + 1)
x = x1
generate_jacobi_plots(A, x, b, fname1="initial_error4.pdf", fname2="final_error4.pdf")

k = 64
tmp1 = np.linspace(0, k*np.pi, n)
x1 = 0.5 * (np.sin(tmp1) + 1)
x = x1
generate_jacobi_plots(A, x, b, fname1="initial_error5.pdf", fname2="final_error5.pdf")


k = 4
tmp1 = np.linspace(0, k*np.pi, n)
x1 = 0.5 * (np.sin(tmp1) + 1)
tmp2 = np.linspace(0, 32 * k * np.pi, n)
x2 = 0.05 * (np.sin(tmp2) + 1)
x = x1+x2
generate_jacobi_plots(A, x, b, fname1="initial_error6.pdf", fname2="final_error6.pdf")
