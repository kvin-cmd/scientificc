import numpy as np
import matplotlib.pyplot as plt

# Logistic growth of fish in a pond (Euler's method):
# dP/dt = r * P * (1 - P / K)
r = 0.5        # growth rate per month
K = 1000.0     # pond capacity (fish)
P0 = 50.0      # starting number of fish
h = 1.0        # step size in months
end_time = 24.0

def growth_rate(P):
    return r * P * (1 - P / K)

time = np.arange(0, end_time + h, h)
fish = np.zeros_like(time)
fish[0] = P0

for i in range(len(time) - 1):
    fish[i + 1] = fish[i] + h * growth_rate(fish[i])

# Exact logistic solution for validation
exact = K / (1 + ((K - P0) / P0) * np.exp(-r * time))

print(f"Euler fish after {end_time:.0f} months: {fish[-1]:.1f}")
print(f"Exact fish after {end_time:.0f} months: {exact[-1]:.1f}")
print(f"Largest error over the period: {np.max(np.abs(fish - exact)):.1f} fish")
print(f"Month when Euler first exceeds 500 fish: "
      f"{time[np.argmax(fish > 500)]:.0f}")

plt.plot(time, fish, marker="o", label="Euler")
plt.plot(time, exact, label="Exact solution")
plt.axhline(K, linewidth=0.8, linestyle="--")
plt.xlabel("Time (months)")
plt.ylabel("Number of fish")
plt.title("Fish pond population growth")
plt.legend()
plt.grid(True)
plt.savefig("docs/task_17_modified.png", dpi=100)
plt.show()