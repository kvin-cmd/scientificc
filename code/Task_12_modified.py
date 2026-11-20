import numpy as np
from scipy.optimize import root

# A cell tower covers a circle of radius 5 km, centred at (0, 0).
# A road follows the curve y = 0.1*x^2 - 3 (distances in km).
# Find where the road enters and leaves the coverage area.
radius = 5.0

def equations(z):
    x, y = z
    return [
        x**2 + y**2 - radius**2,
        y - (0.1 * x**2 - 3)
    ]

for guess in ([4.0, 0.0], [-4.0, 0.0]):
    solution = root(equations, guess)
    print("Initial guess:", guess)
    print("Intersection (km):", np.round(solution.x, 4))
    print("Residuals:", equations(solution.x))
    print("Converged:", solution.success)
    print()