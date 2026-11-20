# Task 16: Numerical Integration

## Inputs and operation
**Input:** smart-meter power readings in kW (0.8, 1.0, 1.4, 1.8, 1.6, 1.2, 0.9) taken every 2 hours from hour 0 to hour 12.

**Operation:** the energy used is the integral of power over time (the area under the power curve), in kWh. Two rules estimate it:
- **Trapezoidal rule:** joins the readings with straight lines and adds up the areas of the trapezoids.
- **Simpson's rule:** fits parabolas through groups of three points, which is usually more accurate for smooth curves.

**Original output:**
```
Energy using trapezoidal rule: 15.700 kWh
Energy using Simpson's rule: 15.800 kWh
Difference between estimates: 0.100 kWh
```

## Parameter change
**Change 1: the peak reading changed from 1.8 to 3.0 kW**
```
Energy using trapezoidal rule: 18.100 kWh
Energy using Simpson's rule: 19.000 kWh
Difference between estimates: 0.900 kWh
```
A higher peak means more energy (15.7 to 18.1 kWh with the trapezoidal rule). The two rules also disagree more (0.9 kWh instead of 0.1), because the curve is now sharper and straight lines fit it worse.

**Change 2: readings every hour (0 to 6 h) instead of every two hours (0 to 12 h)**
```
Energy using trapezoidal rule: 7.850 kWh
Energy using Simpson's rule: 7.900 kWh
Difference between estimates: 0.050 kWh
```
The same power values now cover 6 hours instead of 12, so the energy is about half (15.7 to 7.85 kWh). Energy is power multiplied by time, so the time span matters as much as the power.

## Meaning of the output
The household used about 15.8 kWh over the 12 hours (an average of about 1.3 kW). Power in kW multiplied by time in hours gives energy in kWh. The two rules agree to within 0.1 kWh, which is under 1%, so either is accurate enough here. This task has no graph.

## New case: energy from a solar panel
**Assumptions:** a solar panel's output follows P(t) = 3·sin(π(t − 6)/12) kW from 06:00 to 18:00. This is an assumed model of a sunny day, and it has an exact answer, 72/π = 22.9183 kWh, which lets us measure the errors. Readings are taken every 2 hours. The code is in `code/Task_16_modified.py`.

**Output:**
```
Readings every 2 h (7 readings)
Exact energy: 22.9183 kWh
Trapezoidal rule: 22.3923 kWh (error 0.5260)
Simpson's rule: 22.9282 kWh (error 0.0099)
```

**Parameter change:** readings every 3 hours instead of every 2.
```
Readings every 3 h (5 readings)
Exact energy: 22.9183 kWh
Trapezoidal rule: 21.7279 kWh (error 1.1904)
Simpson's rule: 22.9706 kWh (error 0.0523)
```
With fewer readings, both errors grew: the trapezoidal error from 0.526 to 1.190 kWh, and Simpson's from 0.0099 to 0.0523 kWh.

**Interpretation:** the panel produces about 22.9 kWh in a day. Simpson's rule is much more accurate than the trapezoidal rule (an error of 0.01 kWh against 0.53 kWh), because the output is a smooth curve. The trapezoidal rule underestimates here because its straight lines cut below the curve at the top of the arch. Taking readings more often reduces the error for both rules.