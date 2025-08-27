import numpy as np
matrix=np.random.randint(1, 101, size=(5, 5))
print("5x5 Matrix:")
print(matrix)

max=np.max(matrix)
min=np.min(matrix)
mean=np.mean(matrix)

print(f"\nMaximum value: {max}")
print(f"Minimum value: {min}")
print(f"Mean value: {mean:.2f}")

normal=(matrix-min) / (max-min)
print("\nNormalized Matrix:")
print(normal)

flat= np.sort(matrix.flatten())
print("\nFlattened & Sorted 1D Array:")
print(flat)