# Task 12: Polynomial and Nonlinear Equation Solving

## Inputs and operation
**Input:** two equations in x and y: a circle x² + y² = 4 and a parabola y = x² − 1. The function `equations` returns the two residuals (left side minus right side), which are zero when both equations hold. The solver starts from two initial guesses, [1, 1] and [−1, 1].

**Operation:** `scipy.optimize.root` adjusts x and y until both residuals are close to zero. For each answer the program prints the residuals and whether the solver converged.

**Original output:**
```
Initial guess: [1.0, 1.0]
Intersection: [1.51748991 1.30277564]
Residuals: [np.float64(-2.4780177909633494e-13), np.float64(-2.4158453015843406e-13)]
Converged: True

Initial guess: [-1.0, 1.0]
Intersection: [-1.51748991  1.30277564]
Residuals: [np.float64(-2.4780177909633494e-13), np.float64(-2.4158453015843406e-13)]
Converged: True
```

## Parameter change
**Change 1: circle radius from 2 to 3 (x² + y² = 9)**
```
Initial guess: [1.0, 1.0]
Intersection: [1.83637723 2.37228132]
Residuals: [np.float64(-1.3891110484109959e-12), np.float64(1.4597212327771558e-12)]
Converged: True

Initial guess: [-1.0, 1.0]
Intersection: [-1.83637723  2.37228132]
Residuals: [np.float64(-1.3855583347321954e-12), np.float64(1.4601653219870059e-12)]
Converged: True
```
A bigger circle moves the intersection points up and outwards, from (±1.517, 1.303) to (±1.836, 2.372). The residuals are still tiny, so the answers are valid.

**Change 2: a third starting guess [0, −2]**
```
Initial guess: [0.0, -2.0]
Intersection: [ 0. -2.]
Residuals: [np.float64(0.0), np.float64(-1.0)]
Converged: False
```
The first two guesses gave the same answers as before. The third guess failed: the solver stayed at (0, −2), the second residual is −1 (not zero), and `Converged` is False. At x = 0 the solver cannot improve the guess, because the slope information it needs (the Jacobian) is singular there. So the starting guess matters, and the `Converged` flag must always be checked.

## Meaning of the output
The circle and the parabola cross at two points, (1.517, 1.303) and (−1.517, 1.303). They are mirror images because both equations only depend on x². Both residuals are about 1e-13, which means the answers satisfy both equations to within rounding error (Task 4). The solver finds one intersection per starting guess, so more than one guess is needed to find all the solutions. This task has no graph.

## New case: cell tower coverage and a road
**Assumptions:** a cell tower covers a circle of radius 5 km centred at (0, 0). A road follows y = 0.1x² − 3, in km. These numbers are assumed. The intersections are where the road enters and leaves coverage. The code is in `code/Task_12_modified.py`.

**Output:**
```
Initial guess: [4.0, 0.0]
Intersection (km): [ 4.9721 -0.5279]
Residuals: [np.float64(4.25401935899572e-11), np.float64(1.7763568394002505e-14)]
Converged: True

Initial guess: [-4.0, 0.0]
Intersection (km): [-4.9721 -0.5279]
Residuals: [np.float64(4.25401935899572e-11), np.float64(1.7763568394002505e-14)]
Converged: True
```

**Parameter change:** the coverage radius was reduced from 5 km to 4 km.
```
Initial guess: [4.0, 0.0]
Intersection (km): [ 3.6285 -1.6834]
Residuals: [np.float64(-2.6290081223123707e-13), np.float64(-6.661338147750939e-16)]
Converged: True

Initial guess: [-4.0, 0.0]
Intersection (km): [-3.6285 -1.6834]
Residuals: [np.float64(-2.6290081223123707e-13), np.float64(-6.661338147750939e-16)]
Converged: True
```
With a smaller radius, the road enters and leaves coverage at (±3.63, −1.68) instead of (±4.97, −0.53).

**Interpretation:** the road is inside the coverage between x = −4.97 and x = 4.97 km, which is about 10 km of road. Where the road crosses the edge of the circle, the signal gets weaker, so a driver loses coverage at those two points. A smaller radius cuts the covered stretch to about 7.3 km. A network planner could use this to decide where to place a second tower.