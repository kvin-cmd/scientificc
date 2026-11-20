# Task 3: Mathematical Functions and Vectorization

## Inputs and operation
**Input:** 1,000,000 simulated network latency readings between 5 and 250 ms. A fixed random seed (42) makes the readings the same on every run.

**Operation:** convert each reading from milliseconds to seconds (divide by 1000), then square it. This is done in two ways:
1. A Python `for` loop that handles one value at a time.
2. A vectorized NumPy expression that handles all values at once.

The program also times both methods and works out how many times faster the vectorized version is.

**Original output:**
```
First five squared latency values: [0.03787665 0.01266192 0.04637842 0.03092504 0.00078812]
Loop time: 1.1521 s
Vectorized time: 0.0095 s
Approximate speed-up: 121.8x
```

## Parameter change
I changed the number of readings from 1,000,000 to 100,000 in the line `latency_ms = rng.uniform(5, 250, 1_000_000)`.

**New output:**
```
First five squared latency values: [0.03787665 0.01266192 0.04637842 0.03092504 0.00078812]
Loop time: 0.0614 s
Vectorized time: 0.0018 s
Approximate speed-up: 35.0x
```

- **First five values:** they stayed the same because the random seed is fixed, so the smaller dataset starts with the same numbers.
- **Loop time:** it fell from 1.1521 s to 0.0614 s, because the loop has 10 times fewer values to process. It fell by more than 10 times, which can happen because large loops also put more load on memory. Timings vary a little between runs, so these numbers are not exact.
- **Vectorized time:** it fell from 0.0095 s to 0.0018 s.
- **Speed-up:** it dropped from about 122x to 35x. Vectorized code is still much faster, but its advantage is bigger on large data because it has a small fixed cost that matters more when the data is small.

## Meaning of the output
The squared values are small because the readings are converted to seconds first. For example, 5 ms is 0.005 s, and 0.005² = 0.000025.

Both methods give the same answer. The vectorized version is far faster (about 122x in my run) because NumPy does the repeated arithmetic in fast compiled code, while the Python loop handles each value separately. Vectorization matters most when the same operation is repeated on millions of values. This task has no graph.

## New case: shop prices with VAT
**Assumptions:**
- A shop has 1,000,000 products with random prices between 50 and 5,000 KES.
- VAT is 16%.
- The exchange rate is 129 KES per USD (an assumed value, not a live rate).
- Each price is converted with: price × (1 + VAT) ÷ exchange rate.

**Input data:** 1,000,000 random prices generated with seed 7. The code is in `code/Task_03_modified.py`.

**Output (VAT = 16%):**
```
First five prices in USD: [28.27362922 40.38605926 34.97664522 10.47395105 13.81050239]
Same answer as loop: True
Loop time: 0.9005 s
Vectorized time: 0.0151 s
Approximate speed-up: 59.5x
```

**Parameter change:** I changed VAT from 16% to 20%.
```
First five prices in USD: [29.24858195 41.778682   36.18273643 10.83512177 14.28672661]
Same answer as loop: True
Loop time: 0.9185 s
Vectorized time: 0.0134 s
Approximate speed-up: 68.5x
```
Every price rose by the same factor, 1.20 ÷ 1.16 ≈ 1.034 (about 3.4%). For example, the first price went from 28.27 to 29.25 USD, and the second from 40.39 to 41.78 USD. The speed-up stayed in the same range because the amount of work did not change.

**Interpretation:** The loop and the vectorized version give identical prices ("Same answer as loop: True"), but the vectorized version is about 60x faster. For a shop with millions of products, that is the difference between waiting about a second and waiting almost no time whenever the tax rate or exchange rate changes.