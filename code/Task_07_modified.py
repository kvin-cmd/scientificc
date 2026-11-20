import numpy as np
from scipy.linalg import lu_factor, lu_solve

# Three-loop electrical circuit (mesh-current analysis).
# Unknowns: loop currents I1, I2, I3 in amps.
# The resistor network is fixed, so R is the same every time.
R = np.array([
    [10.0, -4.0,  0.0],
    [-4.0, 12.0, -5.0],
    [ 0.0, -5.0,  9.0]
])

# Battery voltage in each loop for three different settings (volts)
voltage_settings = {
    "Low (6 V)":     np.array([6.0, 0.0, 0.0]),
    "Normal (12 V)": np.array([12.0, 0.0, 0.0]),
    "High (24 V)":   np.array([24.0, 0.0, 0.0])
}

# Factor the resistance matrix only once
lu, piv = lu_factor(R)

for name, v in voltage_settings.items():
    currents = lu_solve((lu, piv), v)
    residual = v - R @ currents
    print(name)
    print("Loop currents (A):", np.round(currents, 4))
    print("Residual norm:", np.linalg.norm(residual))
    print()