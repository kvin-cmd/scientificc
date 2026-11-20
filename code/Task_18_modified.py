import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# A water tank draining through a tap (Torricelli's law):
# dh/dt = -k * sqrt(h)
k = 0.05       # outflow constant
h0 = 4.0       # starting water height (m)

def draining(t, h):
    return [-k * np.sqrt(max(h[0], 0.0))]

# Stop the solver when the tank is empty
def tank_empty(t, h):
    return h[0] - 1e-6
tank_empty.terminal = True
tank_empty.direction = -1

t_eval = np.linspace(0, 100, 400)
solution = solve_ivp(
    draining, (0, 100), [h0],
    t_eval=t_eval, events=tank_empty, rtol=1e-9, atol=1e-11
)

# Exact solution: h(t) = (sqrt(h0) - k*t/2)^2, empty at t = 2*sqrt(h0)/k
exact_empty = 2 * np.sqrt(h0) / k
exact = (np.sqrt(h0) - k * solution.t / 2) ** 2

print("Solver success:", solution.success)
print(f"Tank empty at (solver): {solution.t_events[0][0]:.2f} s")
print(f"Tank empty at (exact):  {exact_empty:.2f} s")
print(f"Height after 20 s: {np.interp(20, solution.t, solution.y[0]):.3f} m")
print(f"Maximum error against exact solution: {np.max(np.abs(solution.y[0]-exact)):.3e} m")

plt.plot(solution.t, solution.y[0], label="solve_ivp")
plt.plot(solution.t, exact, linestyle="--", label="Exact")
plt.xlabel("Time (s)")
plt.ylabel("Water height (m)")
plt.title("Tank draining through a tap")
plt.legend()
plt.grid(True)
plt.savefig("docs/task_18_modified.png", dpi=100)
plt.show()