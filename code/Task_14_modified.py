import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Monthly active users (thousands) of a new mobile-money app
months = np.array([1, 2, 3, 4, 5, 6, 7, 8], dtype=float)
users_k = np.array([12, 15, 18, 23, 28, 36, 44, 55], dtype=float)

# Exponential growth model: users = a * exp(b * month)
def model(x, a, b):
    return a * np.exp(b * x)

parameters, covariance = curve_fit(model, months, users_k, p0=[10, 0.2])
a, b = parameters

predicted = model(months, a, b)
rmse = np.sqrt(np.mean((users_k - predicted)**2))

print(f"Fitted model: users = {a:.3f} * exp({b:.4f} * month)")
print(f"RMSE: {rmse:.2f} thousand users")
print(f"Monthly growth rate: {np.exp(b) - 1:.1%}")
print(f"Predicted users at month 12: {model(12, a, b):.1f} thousand")

x_plot = np.linspace(1, 12, 300)
plt.scatter(months, users_k, label="Observed")
plt.plot(x_plot, model(x_plot, a, b), label="Fitted curve")
plt.xlabel("Month")
plt.ylabel("Active users (thousands)")
plt.title("App user growth: exponential fit")
plt.legend()
plt.grid(True)
plt.savefig("docs/task_14_modified.png", dpi=100)
plt.show()