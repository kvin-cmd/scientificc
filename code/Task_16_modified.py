import numpy as np
from scipy.integrate import simpson

# A solar panel's power output (kW) between 06:00 and 18:00.
# Modelled as P(t) = 3 * sin(pi * (t - 6) / 12), so the exact energy is known:
# integral = 3 * 12 * 2 / pi = 22.918 kWh
def power(t):
    return 3 * np.sin(np.pi * (t - 6) / 12)

exact = 72 / np.pi

step = 2.0   # hours between meter readings
time_hours = np.arange(6, 18 + step, step)
power_kw = power(time_hours)

energy_trapezoid = np.trapezoid(power_kw, time_hours)
energy_simpson = simpson(power_kw, x=time_hours)

print(f"Readings every {step:.0f} h ({len(time_hours)} readings)")
print(f"Exact energy: {exact:.4f} kWh")
print(f"Trapezoidal rule: {energy_trapezoid:.4f} kWh "
      f"(error {abs(energy_trapezoid - exact):.4f})")
print(f"Simpson's rule: {energy_simpson:.4f} kWh "
      f"(error {abs(energy_simpson - exact):.4f})")