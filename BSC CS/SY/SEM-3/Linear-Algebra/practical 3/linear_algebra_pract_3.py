import numpy as np

# Addition, subtraction and mutiplication of Two Matrix
a = np.array([[1,2], [3,4]])
b = np.array([[5,6], [7,8]])
print("The Matrix a is :")
print(a)
print("The Matrix b is :")
print(b)

print("Addition of two matrix a and b is : ")
print(a+b)

print("Subtraction of two matrix a and b is : ")
print(a-b)

print("Multiplication of two matrix a and b is : ")
print(a*b)

# Check if matrix is invertible. 
M = np.array([[5,7], [2,3]])

print("Matrix M = ")
print(M)

c = np.linalg.det(M)
print("Determinant = ", c)

if(c != 0):
    i = np.linalg.inv(M)
    print("Inverse of Matrix M = ")
    print(i)
else:
    print("Matrix M is invertible")
