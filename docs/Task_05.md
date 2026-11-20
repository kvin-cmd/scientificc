# Task 5: Matrix Algebra and Matrix Operations

## Inputs and operation
**Input:** the four corners of a unit square, a rotation angle of 45°, and scale factors of 2.0 (x direction) and 1.5 (y direction).

**Operation:** the program builds a rotation matrix and a scaling matrix, multiplies them with `@` into one combined transformation matrix, and applies it to all four corners at once. It also calculates the determinant. The points are stored as rows, so they are multiplied by the transpose (`.T`) of the matrix.

**Original output:**
```
Original points:
 [[0. 0.]
 [1. 0.]
 [1. 1.]
 [0. 1.]]
Transformation matrix:
 [[ 1.41421356 -1.06066017]
 [ 1.41421356  1.06066017]]
Transformed points:
 [[ 0.          0.        ]
 [ 1.41421356  1.41421356]
 [ 0.35355339  2.47487373]
 [-1.06066017  1.06066017]]
Determinant: 3.000000000000001
```

## Parameter change
**Change 1: angle from 45° to 90°**
```
Transformation matrix:
 [[ 1.22464680e-16 -1.50000000e+00]
 [ 2.00000000e+00  9.18485099e-17]]
Transformed points:
 [[ 0.00000000e+00  0.00000000e+00]
 [ 1.22464680e-16  2.00000000e+00]
 [-1.50000000e+00  2.00000000e+00]
 [-1.50000000e+00  9.18485099e-17]]
Determinant: 2.9999999999999996
```
The square is turned a quarter turn, with corners at about (0, 0), (0, 2), (-1.5, 2) and (-1.5, 0). Values like `1.2e-16` are floating-point rounding for what should be exact zeros (the same effect as in Task 4). The determinant is still 3, because rotation does not change area.

**Change 2: x scale from 2.0 to 3.0** (the angle was still 90° in this run)
```
Transformation matrix:
 [[ 1.83697020e-16 -1.50000000e+00]
 [ 3.00000000e+00  9.18485099e-17]]
Transformed points:
 [[ 0.00000000e+00  0.00000000e+00]
 [ 1.83697020e-16  3.00000000e+00]
 [-1.50000000e+00  3.00000000e+00]
 [-1.50000000e+00  9.18485099e-17]]
Determinant: 4.5
```
The shape is stretched further and the determinant rose from 3 to 4.5, which is 3.0 × 1.5.

## Meaning of the output
Each corner is a coordinate vector. Multiplying by the transformation matrix rotates and stretches it, so one matrix moves all four corners consistently. `.T` is needed because the points are stored as rows, while the matrix is written for column vectors.

The determinant is the area scaling factor. A rotation has a determinant of 1, so it never changes area. The scaling gives 2 × 1.5 = 3, so the new shape has 3 times the area of the unit square. The determinant prints as 3.000000000000001 in one run and 2.9999999999999996 in another because of rounding. This task has no graph.

## New case: rotating and stretching a farm plot
**Assumptions:** a rectangular plot of 100 m by 50 m is rotated by 30° to line up with a road, and stretched by 1.2 in x and shrunk by 0.8 in y, as on a distorted map. The code is in `code/Task_05_modified.py`.

**Output (30°, scale 1.2 and 0.8):**
```
Original corners:
 [[  0.   0.]
 [100.   0.]
 [100.  50.]
 [  0.  50.]]
Transformed corners:
 [[  0.           0.        ]
 [103.92304845  60.        ]
 [ 83.92304845  94.64101615]
 [-20.          34.64101615]]
Determinant: 0.9600000000000001
Original area: 5000.0
New area: 4800.000000000001
Original area x determinant: 4800.0
```

**Parameter change 1: angle from 30° to 60°**
```
Transformed corners:
 [[  0.           0.        ]
 [ 60.         103.92304845]
 [ 25.35898385 123.92304845]
 [-34.64101615  20.        ]]
Determinant: 0.9600000000000001
Original area: 5000.0
New area: 4800.0
Original area x determinant: 4800.0
```
The corners move, but the area stays 4800, because rotation does not change area.

**Parameter change 2: scale 1.0 and 1.0 (angle 30°)**
```
Transformed corners:
 [[  0.           0.        ]
 [ 86.60254038  50.        ]
 [ 61.60254038  93.30127019]
 [-25.          43.30127019]]
Determinant: 1.0
Original area: 5000.0
New area: 5000.0
Original area x determinant: 5000.0
```
With no scaling it is a pure rotation, so the determinant is 1 and the area is the original 5000 m².

**Interpretation:** "Original area x determinant" (4800) equals the new area (4800), which shows the determinant is the area scaling factor. The determinant of 0.96 means the plot shrinks to 96% of its area on the distorted map: 5000 m² becomes 4800 m².