import numpy as np
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt

# Break-even point for a new product at a small shop.
# q = units sold per day.
# Revenue grows with diminishing returns (customers saturate),
# cost grows linearly, plus a fixed daily cost of 600 KES.
def profit(q):
    return 300*np.log(1 + q) - 2.5*q - 600

# Bisection: profit is negative at q=1 and positive at q=10
solution = root_scalar(profit, bracket=[1, 10], method="bisect", xtol=1e-10)

# Fixed-point form: q = exp((600 + 2.5 q)/300) - 1
def g(q):
    return np.exp((600 + 2.5*q) / 300) - 1

q = 5.0
history = [q]
for _ in range(100):
    q_new = g(q)
    history.append(q_new)
    if abs(q_new - q) < 1e-10:
        break
    q = q_new

print(f"Bisection break-even: {solution.root:.4f} units per day")
print(f"Fixed-point break-even: {history[-1]:.4f} units per day")
print("Bisection iterations:", solution.iterations)
print("Fixed-point iterations:", len(history) - 1)
print(f"Profit at break-even: {profit(solution.root):.8f} KES")

qs = np.linspace(1, 60, 300)
plt.plot(qs, profit(qs))
plt.axhline(0, linewidth=0.8)
plt.axvline(solution.root, linestyle="--")
plt.xlabel("Units sold per day")
plt.ylabel("Daily profit (KES)")
plt.title("Break-even point")
plt.grid(True)
plt.savefig("docs/task_10_modified.png", dpi=100)
plt.show()