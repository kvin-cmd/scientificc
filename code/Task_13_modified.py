import numpy as np
from scipy.interpolate import interp1d, CubicSpline
import matplotlib.pyplot as plt

# Water level (cm) in a village borehole tank, measured every 3 hours
hours = np.array([0, 3, 6, 9, 12, 15, 18, 21, 24], dtype=float)
level_cm = np.array([120, 98, 74, 105, 140, 128, 96, 80, 112], dtype=float)
# (the level drops as people draw water, and rises when the pump runs)

linear = interp1d(hours, level_cm, kind="linear")
cubic = CubicSpline(hours, level_cm)

# Estimate every 30 minutes
fine_times = np.arange(0, 24 + 0.5, 0.5)
linear_estimates = linear(fine_times)
cubic_estimates = cubic(fine_times)

target_time = 10.5   # 10:30
print(f"Linear estimate at 10:30: {float(linear(target_time)):.2f} cm")
print(f"Cubic estimate at 10:30: {float(cubic(target_time)):.2f} cm")
print(f"Lowest cubic estimate: {cubic_estimates.min():.2f} cm "
      f"at hour {fine_times[cubic_estimates.argmin()]:.1f}")

plt.scatter(hours, level_cm, label="Measurements (every 3 h)")
plt.plot(fine_times, linear_estimates, label="Linear")
plt.plot(fine_times, cubic_estimates, label="Cubic spline")
plt.xlabel("Hour of day")
plt.ylabel("Tank water level (cm)")
plt.title("Borehole tank level interpolation")
plt.legend()
plt.grid(True)
plt.savefig("docs/task_13_modified.png", dpi=100)
plt.show()