import numpy as np
from scipy.stats import poisson
import matplotlib.pyplot as plt

# A clinic receives a random number of patients per day (Poisson demand).
# It can treat 60 patients per day. How often is it overwhelmed?
rng = np.random.default_rng(42)

capacity = 60
mean_patients = 48
N = 100_000

patients = rng.poisson(mean_patients, N)
overwhelmed = patients > capacity
probability = overwhelmed.mean()

# Exact probability for validation: P(patients > capacity)
exact = poisson.sf(capacity, mean_patients)

print(f"Estimated overwhelmed probability: {probability:.4%}")
print(f"Exact probability: {exact:.4%}")
print(f"Overwhelmed days: {overwhelmed.sum()} out of {N}")
print(f"Expected overwhelmed days per year: {probability*365:.1f}")

running = np.cumsum(overwhelmed) / np.arange(1, N + 1)
indices = np.unique(np.logspace(1, np.log10(N), 200).astype(int)) - 1

plt.semilogx(indices + 1, running[indices], label="Monte Carlo estimate")
plt.axhline(exact, linestyle="--", label="Exact value")
plt.xlabel("Number of simulated days")
plt.ylabel("Estimated probability")
plt.title("Clinic overload risk: Monte Carlo")
plt.legend()
plt.grid(True)
plt.savefig("docs/task_20_modified.png", dpi=100)
plt.show()