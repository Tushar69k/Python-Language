# write a program to add two matrices using NumPy.

import numpy as np

# Creating two matrices
A = np.array([[1, 2, 3],
              [4, 5, 6]])

B = np.array([[7, 8, 9],
              [1, 2, 3]])

# Adding matrices
C = A + B

# Display results
print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nSum of A and B:")
print(C)
