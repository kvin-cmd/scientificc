# Task 11: Root Finding: Newton-Raphson and Secant Methods

## Inputs and operation
**Input:** an investment of 10,000 followed by four yearly cash inflows of 3,000, 3,500, 4,000 and 2,500. The program also has a function `npv(rate)` (net present value) and its derivative `d_npv(rate)`.

**Operation:** the internal rate of return (IRR) is the interest rate at which NPV = 0, so it is a root of `npv(rate)`.
- **Newton-Raphson:** starts at 10% and repeatedly improves the guess with x_new = x − f(x)/f′(x), using the derivative.
- **Secant method:** starts at 5% and 20% and estimates the slope from the last two points, so no derivative is needed.

**Original output:**
```
IRR using Newton-Raphson: 11.542461%
IRR using Secant method: 11.542461%
NPV at Newton solution: 0.000000
Newton iterations: 4
Secant iterations: 7
```

## Parameter change
**Change 1: cash inflows changed to 2,000, 2,500, 3,000 and 2,500**
```
IRR using Newton-Raphson: -0.000000%
IRR using Secant method: 0.000000%
NPV at Newton solution: 0.000000
Newton iterations: 5
Secant iterations: 7
```
The four inflows now add up to exactly 10,000, the same as the investment, so the investor only gets their money back and the IRR is 0%. (The `-0.000000%` is rounding of a tiny negative number.) Smaller inflows give a lower IRR (it fell from 11.54% to 0%).

**Change 2: Newton starting guess from 10% to 90%**
```
IRR using Newton-Raphson: -154.411050%
IRR using Secant method: 11.542461%
NPV at Newton solution: 0.000000
Newton iterations: 12
Secant iterations: 7
```
Newton-Raphson converged to a different root, −154.4%, which is a mathematical solution but is meaningless as an interest rate. A poor starting guess can send Newton to the wrong root. The secant method, with its unchanged starting points, still gave 11.54%.

**Change 3: Newton starting guess from 10% to 50%**
```
IRR using Newton-Raphson: 11.542461%
IRR using Secant method: 11.542461%
NPV at Newton solution: 0.000000
Newton iterations: 8
Secant iterations: 7
```
This start still reaches the correct answer, but it needs 8 iterations instead of 4. The further the start is from the root, the more iterations are needed.

## Meaning of the output
The IRR is 11.54% per year: if the money earned that rate every year, the investment of 10,000 would grow to exactly match the cash inflows. At that rate the NPV is zero, which confirms it is the root. The project is worth doing if the investor could not earn more than 11.54% elsewhere. Both methods give the same answer. Newton took 4 iterations and the secant method 7, so Newton was faster here, but it needs the derivative. This task has no graph.

## New case: a farmer buying a dairy cow
**Assumptions:** a farmer buys a cow for 120,000 KES. The net milk income is 30,000, 36,000, 40,000, 40,000 and 65,000 KES in years 1 to 5 (the last includes selling the cow). These numbers are assumed. The farmer compares the IRR with a 12% bank rate. The code is in `code/Task_11_modified.py`.

**Output:**
```
IRR using Newton-Raphson: 19.5141%
IRR using Secant method: 19.5141%
NPV at Newton solution: -0.000000
Newton iterations: 5
Secant iterations: 7
NPV at a 12% bank rate: 26259.37 KES
```

**Parameter change:** the cash flows were lowered to 25,000, 30,000, 33,000, 33,000 and 60,000 KES.
```
IRR using Newton-Raphson: 13.3865%
IRR using Secant method: 13.3865%
NPV at Newton solution: -0.000000
Newton iterations: 5
Secant iterations: 7
NPV at a 12% bank rate: 4743.70 KES
```
Lower income dropped the IRR from 19.51% to 13.39%, and the NPV at 12% dropped from 26,259 to 4,744 KES.

**Interpretation:** the cow earns about 19.5% a year, well above the 12% bank rate, so it is a good investment (positive NPV of about 26,259 KES at 12%). With lower milk income the return falls to 13.4%, which is barely above the bank rate (the NPV is still positive but small). So the investment is sensitive to income, and the farmer should check how reliable the milk sales are.