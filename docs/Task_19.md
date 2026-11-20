# Task 19: Numerical Optimization

## Inputs and operation
**Input:** two server types. Type A costs 12 per unit and gives 100 units of capacity. Type B costs 18 per unit and gives 170. The total capacity must be at least 1000. The starting guess is (5, 3).

**Operation:** `scipy.optimize.minimize` (method SLSQP) minimises the cost 12x + 18y, subject to the constraint 100x + 170y − 1000 ≥ 0 and bounds x, y ≥ 0. The program then searches whole-number combinations of servers for the cheapest one that meets the capacity.

**Original output:**
```
Optimization success: True
Type A allocation: 0.000
Type B allocation: 5.882
Total capacity: 1000.00
Minimum planning cost: 105.88
Best nearby integer solution: (108, 0, 6, 1020)
```

## Parameter change
**Change 1: required capacity from 1000 to 2000**
```
Optimization success: True
Type A allocation: 0.000
Type B allocation: 11.765
Total capacity: 2000.00
Minimum planning cost: 211.76
Best nearby integer solution: (216, 0, 12, 2040)
```
Doubling the requirement doubles the allocation and the cost (105.88 to 211.76), because the cost is linear in the capacity.

**Change 2: the cost of Type A reduced from 12 to 8**
```
Optimization success: True
Type A allocation: 10.000
Type B allocation: 0.000
Total capacity: 1000.00
Minimum planning cost: 80.00
Best nearby integer solution: (80, 10, 0, 1000)
```
The optimum switched from Type B to Type A. Cost per unit of capacity is 12/100 = 0.12 for A and 18/170 = 0.106 for B in the original, so B was cheaper. With A at 8, it is 0.08, so A is now cheaper, and the cost fell to 80.

## Meaning of the output
The cheapest way to reach 1000 units of capacity is to buy only Type B (5.882 units), at a cost of 105.88. Type B gives more capacity per unit of money. The total capacity is exactly 1000, which means the constraint is "active": the solver buys no more than needed. Whole servers cannot be fractional, so the best whole-number plan is 6 Type B servers, with capacity 1020 and cost 108, slightly above the continuous optimum. This task has no graph.

## New case: cheapest daily feed for a dairy cow
**Assumptions:** a cow needs at least 1.2 kg of protein and 100 MJ of energy a day. Maize bran costs 40 KES per kg and gives 0.08 kg protein and 12 MJ per kg. Sunflower cake costs 70 KES per kg and gives 0.35 kg protein and 9 MJ per kg. All numbers are assumed. The code is in `code/Task_19_modified.py`.

**Output:**
```
Optimization success: True
Maize bran: 6.954 kg
Sunflower cake: 1.839 kg
Protein supplied: 1.200 kg (need 1.2)
Energy supplied: 100.00 MJ (need 100)
Minimum daily cost: 406.90 KES
```

**Parameter change:** the protein requirement was raised from 1.2 kg to 1.8 kg.
```
Optimization success: True
Maize bran: 5.402 kg
Sunflower cake: 3.908 kg
Protein supplied: 1.800 kg (need 1.8)
Energy supplied: 100.00 MJ (need 100)
Minimum daily cost: 489.66 KES
```
Sunflower cake rose from 1.84 to 3.91 kg and bran fell from 6.95 to 5.40 kg, because cake is the protein-rich feed. The daily cost rose by 82.76 KES (406.90 to 489.66).

**Interpretation:** the cheapest feed mix is about 7.0 kg of bran and 1.8 kg of cake, at a cost of 406.90 KES a day. Both nutrient needs are met exactly (1.200 kg protein and 100.00 MJ energy), which means both constraints are active: any cheaper mix would fall short on at least one need. A farmer can use this to see how much more feed will cost if the cow needs more protein.