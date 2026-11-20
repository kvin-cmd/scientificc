# Task 6: Solution of Systems of Linear Equations

## Inputs and operation
**Input:** a coefficient matrix A = [[4, 2], [8, 12]] (CPU and memory used per server of Type A and Type B) and a vector b = [20, 72] (total CPU and memory observed).

**Operation:** the problem is written as Ax = b, where x holds the unknown number of Type A and Type B servers. `np.linalg.solve(A, b)` finds x. The program then checks the answer by computing A @ x and the residual b − A @ x.

**Original output:**
```
Type A servers: 3
Type B servers: 4
Verification A @ solution: [20. 72.]
Residual: [0. 0.]
Residual norm: 0.0
```

## Parameter change
**Change 1: totals from [20, 72] to [24, 96]**
```
Type A servers: 3
Type B servers: 6
Verification A @ solution: [24. 96.]
Residual: [0. 0.]
Residual norm: 0.0
```
Type A stayed at 3 and Type B rose from 4 to 6. More CPU and memory in use means more Type B servers are needed, and a whole-number answer still comes out.

**Change 2: totals from [20, 72] to [22, 72]** (printing with 2 decimals)
```
Type A servers: 3.75
Type B servers: 3.50
Verification A @ solution: [22. 72.]
Residual: [0. 0.]
Residual norm: 0.0
```
The system still has an exact solution, but it is not whole numbers. In real life you cannot have 3.75 servers, so these totals could not come from a real set of servers.

## Meaning of the output
Each equation is one resource: 4x + 2y = 20 for CPU and 8x + 12y = 72 for memory. The solution x = 3, y = 4 is the only pair that satisfies both. Check: 4(3) + 2(4) = 20 and 8(3) + 12(4) = 72. The residual is zero, which means A @ x reproduces b exactly. For larger systems a tiny non-zero residual (about 1e-15) would be normal, because of rounding (Task 4). This task has no graph.

## New case: fertiliser mix for a farm in Thika
**Assumptions:** three fertilisers A, B and C supply nitrogen (N), phosphorus (P) and potassium (K) in different proportions. For example, 1 kg of A supplies 0.20 kg N, 0.10 kg P and 0.05 kg K. The crop needs exactly 30 kg N, 24 kg P and 18 kg K. The proportions are assumed values. The code is in `code/Task_06_modified.py`.

**Output:**
```
Fertiliser A: 120.00 kg
Fertiliser B: 45.00 kg
Fertiliser C: 30.00 kg
Verification A @ solution: [30. 24. 18.]
Residual norm: 0.0
```

**Parameter change:** the potassium need was raised from 18 kg to 30 kg.
```
Fertiliser A: 120.00 kg
Fertiliser B: 15.00 kg
Fertiliser C: 90.00 kg
Verification A @ solution: [30. 24. 30.]
Residual norm: 0.0
```
Fertiliser C (the one richest in potassium) rose from 30 kg to 90 kg, and B fell from 45 kg to 15 kg, while A stayed at 120 kg. The nutrients are linked, so changing one need changes the whole mix.

**Interpretation:** the farmer needs 120 kg of A, 45 kg of B and 30 kg of C to supply exactly the nutrients the crop needs. The zero residual confirms that the mix meets all three targets.