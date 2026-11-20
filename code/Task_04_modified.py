import numpy as np
import math

price = 0.10          # KES per item
n = 1_000_000         # number of items
expected = price * n  # should be 100000.0 (or close)

total = 0.0
for _ in range(n):
    total += price

abs_err = abs(total - 100000.0)

print("Total using a loop:", total)
print("Exactly 100000?", total == 100000.0)
print("Close to 100000?", np.isclose(total, 100000.0))
print(f"Absolute error: {abs_err:.10f}")
print(f"Relative error: {abs_err / 100000.0:.3e}")
print("math.fsum result:", math.fsum([price] * n))

# Safer approach: count whole cents as integers
cents = 0
for _ in range(n):
    cents += 10
print("Using integer cents:", cents / 100)