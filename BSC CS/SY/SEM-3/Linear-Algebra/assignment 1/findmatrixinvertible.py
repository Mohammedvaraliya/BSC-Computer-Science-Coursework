# Write a python program to enter a matrix and check if it is invertible. If invertible exists then find inverse.
import numpy as np

matrix = np.array([[5,2], [10,2]])
print("Matrix M = ")
print(matrix)

c = np.linalg.det(matrix)
print("Determinant = ", c)

if(c != 0):
    i = np.linalg.inv(matrix)
    print("Inverse of Matrix M = ")
    print(i)
    
else:
    print("Matrix M is invertible")