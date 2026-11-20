# Task 4: Floating-Point Arithmetic and Numerical Errors

## Inputs and operation
The program has three parts:
1. **Comparison:** it adds 0.1 + 0.2 and compares the result with 0.3 using `==` and using `np.isclose`.
2. **Error measurement:** it compares the true value of √2 with the approximation 1.414 and calculates the absolute error and the relative error (absolute error ÷ true value).
3. **Stable vs unstable formula:** it evaluates (√(1+x) − 1)/x and 1/(√(1+x) + 1) for x = 1e-4, 1e-8 and 1e-12. The two formulas are algebraically identical, but the first subtracts two nearly equal numbers.

**Original output:**
```
0.1 + 0.2 = 0.30000000000000004
Exact comparison: False
Tolerance-based comparison: True
Absolute error: 0.00021356
Relative error: 0.01510114%
x=1e-04: direct=0.499987500624, stable=0.499987500625
x=1e-08: direct=0.499999996961, stable=0.499999998750
x=1e-12: direct=0.500044450291, stable=0.500000000000
```

## Parameter change
I made two changes: the approximation from 1.414 to 1.41421, and the x list extended with 1e-15 and 1e-16.

**New output:**
```
0.1 + 0.2 = 0.30000000000000004
Exact comparison: False
Tolerance-based comparison: True
Absolute error: 0.00000356
Relative error: 0.00025190%
x=1e-04: direct=0.499987500624, stable=0.499987500625
x=1e-08: direct=0.499999996961, stable=0.499999998750
x=1e-12: direct=0.500044450291, stable=0.500000000000
x=1e-15: direct=0.444089209850, stable=0.500000000000
x=1e-16: direct=0.000000000000, stable=0.500000000000
```
- **Errors:** the absolute error dropped from 0.00021356 to 0.00000356 and the relative error from 0.0151% to 0.00025%, because 1.41421 is much closer to √2 than 1.414.
- **Direct formula:** it gets worse as x shrinks. It is accurate to about 12 digits at 1e-4, but at 1e-12 it gives 0.50004 instead of 0.5, at 1e-15 it gives 0.444, and at 1e-16 it gives 0.
- **Stable formula:** it stays at 0.5 for every x.

## Meaning of the output
Computers store numbers in binary, and 0.1 and 0.2 cannot be written exactly in binary. Their sum is 0.30000000000000004, so `==` says False even though the maths says they are equal. A tolerance comparison (`np.isclose`) is the correct way to compare decimals.

A closer approximation gives a smaller error. The direct formula fails because of **cancellation**: when x is tiny, √(1+x) is almost exactly 1, so subtracting 1 wipes out the correct digits and leaves mostly rounding error. At x = 1e-16, 1 + x is rounded to exactly 1.0, so the answer becomes 0. The stable formula has no subtraction, so it stays accurate. The same maths can behave very differently on a computer depending on how it is written. This task has no graph.

## New case: shop till adding 0.10 KES items
**Assumptions:** a till adds up 1,000,000 items priced 0.10 KES each. The correct total is 100,000.00 KES. I compare a plain loop, `math.fsum`, and counting in whole cents.

**Input data:** price = 0.10, n = 1,000,000. The code is in `code/Task_04_modified.py`.

**Output:**
```
Total using a loop: 100000.00000133288
Exactly 100000? False
Close to 100000? True
Absolute error: 0.0000013329
Relative error: 1.333e-11
math.fsum result: 100000.0
Using integer cents: 100000.0
```

**Parameter change:** I changed the price to 0.25 KES (and the cents step to 25, the target to 250,000).
```
(paste your output here)
```
(Explain: 0.25 is exactly representable in binary, so repeated addition does not build up any error, unlike 0.10.)

**Interpretation:** 0.10 cannot be stored exactly, so every addition adds a tiny error and a million additions accumulate to about 0.0000013 KES. That is negligible here, but it shows why exact `==` checks on money fail. `math.fsum` and integer cents give the exact total, so banking software stores money in whole cents.