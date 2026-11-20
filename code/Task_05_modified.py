import numpy as np

# Corners of a rectangular farm plot in metres: each row is [x, y]
plot = np.array([
    [0.0, 0.0],
    [100.0, 0.0],
    [100.0, 50.0],
    [0.0, 50.0]
])

angle = np.deg2rad(30)

rotation = np.array([
    [np.cos(angle), -np.sin(angle)],
    [np.sin(angle),  np.cos(angle)]
])

scale = np.array([
    [1.2, 0.0],
    [0.0, 0.8]
])

transformation = rotation @ scale
new_plot = plot @ transformation.T

def polygon_area(p):
    x, y = p[:, 0], p[:, 1]
    return 0.5 * abs(np.dot(x, np.roll(y, -1)) - np.dot(y, np.roll(x, -1)))

print("Original corners:\n", plot)
print("Transformed corners:\n", new_plot)
print("Determinant:", np.linalg.det(transformation))
print("Original area:", polygon_area(plot))
print("New area:", polygon_area(new_plot))
print("Original area x determinant:", polygon_area(plot) * np.linalg.det(transformation))