import numpy as np
import matplotlib.pyplot as plt

# Water level in a tank (cm), measured every 10 minutes while the
# tank is first filled by a pump, then drained by a tap.
minutes = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80], dtype=float)
level_cm = np.array([40, 52, 66, 82, 95, 103, 96, 82, 64], dtype=float)

# np.gradient uses central differences inside and one-sided at the ends
rate = np.gradient(level_cm, minutes)   # cm per minute

for t, h, r in zip(minutes, level_cm, rate):
    print(f"t={t:.0f} min, level={h:.0f} cm, rate={r:+.2f} cm/min")

# Forward difference at t=20 for comparison with the central difference
forward = (level_cm[3] - level_cm[2]) / (minutes[3] - minutes[2])
print(f"Forward difference at t=20: {forward:+.2f} cm/min "
      f"(central: {rate[2]:+.2f} cm/min)")

plt.plot(minutes, rate, marker="o")
plt.axhline(0, linewidth=0.8)
plt.xlabel("Time (minutes)")
plt.ylabel("Rate of change of level (cm/min)")
plt.title("Tank level: rate of change")
plt.grid(True)
plt.savefig("docs/task_15_modified.png", dpi=100)
plt.show()