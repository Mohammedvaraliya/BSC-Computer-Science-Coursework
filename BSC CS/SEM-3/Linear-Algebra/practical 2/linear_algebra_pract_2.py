import numpy as np

u = np.array((2,4,5))
v = np.array((3,2,1))
print("The vector u and v is")
print(u)
print(v)

a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))

c = (a*u)+(b*v)
print("The vector au + bv is : ", c)

d = np.dot(u,v)
print("The dot product of u and v is : ", d)