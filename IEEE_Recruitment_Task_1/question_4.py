import numpy as np
matrix=np.random.randint(1, 101, size=(5, 5))
print("5x5 Matrix:")
print(matrix)

middle=matrix[1:4, 1:4]
print("\nMiddle 3x3 Matrix:")
print(middle)

first=middle[0, :] 
last=middle[:, -1]      
print("\nFirst row of 3x3:", first)
print("Last column of 3x3:", last)

dot=np.dot(first, last)
print("\nDot Product of first row and last column:", dot)