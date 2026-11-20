import numpy as np
import timeit

rng = np.random.default_rng(7)
prices_kes = rng.uniform(50, 5000, 1_000_000)

vat_rate = 0.16
kes_per_usd = 129.0   # assumed exchange rate

def loop_version():
    result = []
    for price in prices_kes:
        result.append(price * (1 + vat_rate) / kes_per_usd)
    return result

def vectorized_version():
    return prices_kes * (1 + vat_rate) / kes_per_usd

loop_time = timeit.timeit(loop_version, number=1)
vector_time = timeit.timeit(vectorized_version, number=3) / 3

result = vectorized_version()
print("First five prices in USD:", result[:5])
print("Same answer as loop:", np.allclose(result, loop_version()))
print(f"Loop time: {loop_time:.4f} s")
print(f"Vectorized time: {vector_time:.4f} s")
print(f"Approximate speed-up: {loop_time/vector_time:.1f}x")