import numpy as np

# Fertiliser mix for a farm in Thika.
# x = kg of Fertiliser A, y = kg of Fertiliser B, z = kg of Fertiliser C
# Each row is one nutrient (N, P, K); each column is one fertiliser.
# Entries are the kg of nutrient supplied per kg of fertiliser.
A = np.array([
    [0.20, 0.10, 0.05],   # nitrogen (N)
    [0.10, 0.20, 0.10],   # phosphorus (P)
    [0.05, 0.10, 0.25]    # potassium (K)
])

# Nutrients the crop needs in kg: N, P, K
b = np.array([30.0, 24.0, 18.0])

solution = np.linalg.solve(A, b)
residual = b - A @ solution

print(f"Fertiliser A: {solution[0]:.2f} kg")
print(f"Fertiliser B: {solution[1]:.2f} kg")
print(f"Fertiliser C: {solution[2]:.2f} kg")
print("Verification A @ solution:", A @ solution)
print("Residual norm:", np.linalg.norm(residual))