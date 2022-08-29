# Write a python program for rotating a complex number z=2+3i by 180°
import matplotlib.pyplot as plt
m=2+3j
n=-1
plt.scatter(m.real,m.imag,color='red')
c=m*n
plt.scatter(c.real,c.imag,color='purple')
plt.show()