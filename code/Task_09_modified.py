import numpy as np

# Matatu route network between 6 towns near Nairobi.
# A 1 means there is a direct route between two towns.
# Town order: Nairobi, Thika, Juja, Ruiru, Kiambu, Machakos
towns = ["Nairobi", "Thika", "Juja", "Ruiru", "Kiambu", "Machakos"]

A = np.array([
    [0., 1., 1., 1., 1., 1.],   # Nairobi
    [1., 0., 1., 1., 0., 0.],   # Thika
    [1., 1., 0., 1., 0., 0.],   # Juja
    [1., 1., 1., 0., 1., 0.],   # Ruiru
    [1., 0., 0., 1., 0., 0.],   # Kiambu
    [1., 0., 0., 0., 0., 0.]    # Machakos
])

eigenvalues, eigenvectors = np.linalg.eig(A)

index = np.argmax(np.real(eigenvalues))
dominant_value = np.real(eigenvalues[index])
dominant_vector = np.abs(np.real(eigenvectors[:, index]))
centrality = dominant_vector / dominant_vector.sum()

print("Dominant eigenvalue:", round(dominant_value, 4))
print("Eigenvector-based importance:")
for town, score in sorted(zip(towns, centrality), key=lambda p: -p[1]):
    print(f"{town}: {score:.4f}")

v = np.real(eigenvectors[:, index])
print("Verification error:", np.linalg.norm(A @ v - dominant_value * v))