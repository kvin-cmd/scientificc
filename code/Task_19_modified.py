import numpy as np
from scipy.optimize import minimize

# Daily feed for a dairy cow: choose kg of maize bran (x) and
# sunflower cake (y) to minimise cost while meeting nutrient needs.
#                       Maize bran   Sunflower cake
# Cost (KES per kg):        40            70
# Protein (kg per kg):      0.08          0.35
# Energy (MJ per kg):       12            9
# Daily needs: at least 1.2 kg protein and at least 100 MJ energy.

def cost(z):
    x, y = z
    return 40*x + 70*y

constraints = [
    {"type": "ineq", "fun": lambda z: 0.08*z[0] + 0.35*z[1] - 1.2},   # protein
    {"type": "ineq", "fun": lambda z: 12*z[0] + 9*z[1] - 100}         # energy
]
bounds = [(0, None), (0, None)]

solution = minimize(cost, x0=[8, 3], method="SLSQP",
                    bounds=bounds, constraints=constraints)
x, y = solution.x

print("Optimization success:", solution.success)
print(f"Maize bran: {x:.3f} kg")
print(f"Sunflower cake: {y:.3f} kg")
print(f"Protein supplied: {0.08*x + 0.35*y:.3f} kg (need 1.2)")
print(f"Energy supplied: {12*x + 9*y:.2f} MJ (need 100)")
print(f"Minimum daily cost: {solution.fun:.2f} KES")