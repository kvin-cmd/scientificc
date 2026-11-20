import numpy as np
import matplotlib.pyplot as plt

# Steady-state temperature along a metal rod with 9 interior points.
# One end is held at 80 C (heater), the other at 25 C (room).
n = 9
A = 2 * np.eye(n) - np.eye(n, k=1) - np.eye(n, k=-1)

b = np.zeros(n)
b[0] = 80.0    # heated end
b[-1] = 25.0   # room-temperature end

def jacobi(A, b, tol=1e-8, max_iter=2000):
    D = np.diag(A)
    R = A - np.diagflat(D)
    x = np.zeros_like(b)
    errors = []
    for _ in range(max_iter):
        x_new = (b - R @ x) / D
        error = np.linalg.norm(x_new - x, ord=np.inf)
        errors.append(error)
        if error < tol:
            return x_new, errors
        x = x_new
    return x, errors

def gauss_seidel(A, b, tol=1e-8, max_iter=2000):
    x = np.zeros_like(b)
    errors = []
    for _ in range(max_iter):
        old = x.copy()
        for i in range(len(b)):
            x[i] = (b[i] - A[i, :i] @ x[:i] - A[i, i+1:] @ old[i+1:]) / A[i, i]
        error = np.linalg.norm(x - old, ord=np.inf)
        errors.append(error)
        if error < tol:
            return x, errors
    return x, errors

x_j, err_j = jacobi(A, b)
x_gs, err_gs = gauss_seidel(A, b)
x_exact = np.linalg.solve(A, b)

np.set_printoptions(precision=3, suppress=True)
print("Jacobi temperatures:", x_j)
print("Gauss-Seidel temperatures:", x_gs)
print("Direct solution:", x_exact)
print("Jacobi iterations:", len(err_j))
print("Gauss-Seidel iterations:", len(err_gs))

plt.semilogy(err_j, label="Jacobi")
plt.semilogy(err_gs, label="Gauss-Seidel")
plt.xlabel("Iteration")
plt.ylabel("Maximum change")
plt.title("Rod temperature: convergence")
plt.legend()
plt.grid(True)
plt.savefig("docs/task_08_modified.png", dpi=100)
plt.show()