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

def gauss_seidel(A: sparse.csr_matrix, x: np.array, b: np.array, omega=1.0):
    r = b - A * x
    A_ = A.toarray()
    # L = -np.tril(A_, -1)
    U = -np.triu(A_, 1)
    D = np.matrix(np.diagflat(np.diag(A_)))
    B = D - U
    e = np.linalg.solve(B, omega * r)
    return x + e


def plot_error(e, h, filename):
    x = np.linspace(0+h, 1-h, n)
    y = e
    rc('text', usetex=True)
    sns.set(style="whitegrid")
    sns.set_context("paper")
    sns.despine()
    sns.relplot(x=x, y=y, kind='line', color="black", dashes=False, legend=False)
    plt.tight_layout()
    plt.xlim(0, 1)
    plt.ylim(-1.1, 1.1)
    plt.savefig(filename, dpi=300)


def generate_plots(iterate, h, A, x, b, steps=100, omega=1.0, name="jacobi"):
    e = x - b
    plot_error(e, h, f"initial_error_{name}.pdf")
    for i in range(1, steps + 1):
        # x_new = jacobi(A, x, b, omega)
        x_new = iterate(A, x, b, omega)
        x = x_new
    e = x - b
    plot_error(e, h, f"final_error_{name}.pdf")


h = 1/2**6
n = int(1/h - 1)
omega = 1
steps = 100
A = generate_1D_matrix(n)
b = np.zeros(n)

for i in range(2, 7):
    k = 2**i
    end = k * np.pi
    tmp1 = np.linspace(0 + h * end, end - h * end, n)
    x1 = (np.sin(tmp1))
    x = x1
    generate_plots(jacobi, h, A, x, b, steps=steps, omega=omega, name=f"jacobi_{k}pi_coarse")
    generate_plots(gauss_seidel, h, A, x, b, steps=steps, omega=omega, name=f"gauss_seidel_{k}pi_coarse")

k = 4
tmp1 = np.linspace(0, k*np.pi, n)
x1 = 0.5 * (np.sin(tmp1))
tmp2 = np.linspace(0, 16 * k * np.pi, n)
x2 = 0.5 * (np.sin(tmp2))
x = x1+x2
generate_plots(jacobi, h, A, x, b, steps=steps, omega=omega, name="jacobi_combined_coarse")
generate_plots(gauss_seidel, h, A, x, b, steps=steps, omega=omega, name="gauss_seidel_combined_coarse")
