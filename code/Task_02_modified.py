import numpy as np

# Hourly greenhouse temperatures (C) - replace with your own made-up values
greenhouse_c = np.array([
    16.0, 15.5, 15.2, 15.0, 15.8, 18.0,
    22.0, 26.5, 30.0, 33.5, 35.2, 36.0,
    36.4, 35.8, 34.0, 31.5, 28.0, 25.0,
    22.0, 20.0, 18.5, 17.5, 16.8, 16.2
])

limit_c = 32.0  # crops stress above this

too_hot = greenhouse_c > limit_c        # True/False for each hour
hours_too_hot = too_hot.sum()

print(f"Mean: {greenhouse_c.mean():.2f} C")
print(f"Hottest: {greenhouse_c.max():.1f} C at hour {greenhouse_c.argmax()}")
print(f"Hours above {limit_c} C: {hours_too_hot}")
print("Hot hours (index):", np.where(too_hot)[0])