# Task 7: Gaussian Elimination and LU Decomposition

## Inputs and operation
**Input:** a 3×3 coefficient matrix A = [[4, -1, 0], [-1, 4, -1], [0, -1, 3]] and three different measurement vectors b: [15, 10, 10], [16, 11, 9] and [14, 12, 11].

**Operation:** `lu_factor(A)` splits A into a lower-triangular matrix L and an upper-triangular matrix U (with row swaps recorded in `piv`). This is done only once. `lu_solve` then reuses those factors to solve Ax = b for each measurement vector. The residual b − A @ x checks each answer, and `np.linalg.solve` is used as a comparison.

**Original output:**
```
Measurement set 1
Solution: [5. 5. 5.]
Residual norm: 0.0

Measurement set 2
Solution: [5.31707317 5.26829268 4.75609756]
Residual norm: 1.7763568394002505e-15

Measurement set 3
Solution: [4.90243902 5.6097561  5.53658537]
Residual norm: 0.0

Direct solution for first set: [5. 5. 5.]
```

## Parameter change
**Change 1: first measurement vector from [15, 10, 10] to [30, 20, 20]**
```
Measurement set 1
Solution: [10. 10. 10.]
Residual norm: 0.0
```
(Sets 2 and 3 were unchanged.) Doubling b doubled the solution from [5, 5, 5] to [10, 10, 10]. This is because the system is linear: if b is multiplied by a number, x is multiplied by the same number.

**Change 2: top-left entry of A from 4 to 8**
```
Measurement set 1
Solution: [2.41176471 4.29411765 4.76470588]
Residual norm: 0.0

Measurement set 2
Solution: [2.56470588 4.51764706 4.50588235]
Residual norm: 3.552713678800501e-15

Measurement set 3
Solution: [2.36470588 4.91764706 5.30588235]
Residual norm: 0.0
```
A bigger diagonal entry in the first equation made the first unknown smaller (5 became about 2.41), and it also changed the other two unknowns because the equations are linked. All three solutions changed because they all use the same A, which was refactored.

## Meaning of the output
Each solution is the set of three unknowns that satisfies all three equations at once. For set 1, x = [5, 5, 5] works because 4(5) − 5 = 15, −5 + 4(5) − 5 = 10 and −5 + 3(5) = 10. The residual norms are zero or around 1e-15, which means the answers are correct up to rounding error (Task 4). `lu_solve` and `np.linalg.solve` give the same answer. The advantage of LU is that the expensive step (factoring A) is done once, and each new b only needs two cheap triangular solves. This task has no graph.

## New case: three-loop electrical circuit
**Assumptions:** a circuit with three loops has fixed resistances (the matrix R, in ohms, assumed values). The battery in loop 1 is set to 6 V, 12 V and 24 V. The unknowns are the loop currents in amps. Because R does not change, it is factored once and reused for all three settings. The code is in `code/Task_07_modified.py`.

**Output:**
```
Low (6 V)
Loop currents (A): [0.7259 0.3149 0.1749]
Residual norm: 7.076311083754595e-16

Normal (12 V)
Loop currents (A): [1.4519 0.6297 0.3499]
Residual norm: 1.415262216750919e-15

High (24 V)
Loop currents (A): [2.9038 1.2595 0.6997]
Residual norm: 2.830524433501838e-15
```

**Parameter change:** the last resistance in R was changed from 9 to 20.
```
Low (6 V)
Loop currents (A): [0.7049 0.2623 0.0656]
Residual norm: 1.1188630228279524e-16

Normal (12 V)
Loop currents (A): [1.4098 0.5246 0.1311]
Residual norm: 2.237726045655905e-16

High (24 V)
Loop currents (A): [2.8197 1.0492 0.2623]
Residual norm: 4.47545209131181e-16
```
With more resistance in loop 3, the current there fell a lot (0.1749 A to 0.0656 A at 6 V), and the other two currents fell slightly.

**Interpretation:** when the battery voltage doubles, every current doubles (0.7259 → 1.4519 → 2.9038 A), because the circuit is linear. The engineer factors R once and can then test any battery setting quickly, which is the benefit of LU decomposition when the same circuit is analysed many times.