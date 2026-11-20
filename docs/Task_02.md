# Task 2: NumPy Arrays and Numerical Computation

## Inputs and operation
**Input:** 24 hourly temperature readings in °C, from 18.5 at midnight up to 29.4 at midday and back down to 19.0.

**Operation:** The program stores the readings in one NumPy array. It calculates the mean, minimum and maximum, then converts every value to Fahrenheit in one step using F = 1.8C + 32. This is vectorized, so no loop is needed.

**Original output:**
```
Daily mean temperature: 23.12 C
Minimum temperature: 17.50 C
Maximum temperature: 29.40 C
First six Fahrenheit readings: 65.3, 64.4, 64.04, 63.5, 64.22, 66.2
```

## Parameter change
I changed the peak reading from 29.4 to 35.0 and reran the program.

**New output:**
```
Daily mean temperature: 23.35 C
Minimum temperature: 17.50 C
Maximum temperature: 35.00 C
```
- **Maximum:** it became 35.0 because the reading I changed was the hottest one.
- **Minimum:** it stayed at 17.5 because the coldest reading was not changed.
- **Mean:** it rose from 23.12 to 23.35 because the mean uses every value. The reading went up by 5.6, and 5.6 ÷ 24 ≈ 0.23.

The mean responds to any change, while the min and max only change when the extreme value itself changes.

## Meaning of the output
The day is coolest in the early morning (about 17.5 °C) and warmest around midday (29.4 °C), with an average of 23.12 °C. The Fahrenheit values are the same readings on a different scale. This task has no graph.

## New case: greenhouse
**Assumptions:** A greenhouse is monitored hourly for 24 hours. The crops are stressed when the temperature is above 32 °C. The readings are made-up values for a hot day.

**Input data:** 24 hourly readings from 15.0 °C (early morning) to 36.4 °C (midday). The code is in `code/Task_02_modified.py`.

**Output:**
```
Mean: 24.18 C
Hottest: 36.4 C at hour 12
Hours above 32.0 C: 6
Hot hours (index): [ 9 10 11 12 13 14]
```

**Interpretation:** The greenhouse is too hot for 6 hours in a row, from 09:00 to 14:00, and peaks at midday. The farmer should plan shading or ventilation for those hours.

**Parameter change:** I lowered the limit from 32 to 30 °C. The count rose from 6 to 7 hours, because the 15:00 reading of 31.5 °C now counts as too hot. The 08:00 reading of exactly 30.0 °C does not count, because the comparison is strictly "greater than". A stricter limit means more hours are flagged.