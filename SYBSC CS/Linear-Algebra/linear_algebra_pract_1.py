# 1. Addition of two complex numbers
x = 1+3j
y = 10+3j
print("Addition of two complex numbers is : ", x+y)


# 2. Displaying the conjugate of a complex number
a = 4+2j
print("Conjugate of a given complex number is : ", a.conjugate())


# 3. Plotting a set of complex numbers
import matplotlib.pyplot as plot
x = 2+2j
a = [-4+3j, -2+1j, -5+3.5j, 0+2j, 1+1.5j]
X = [x.real for x in a]
Y = [x.imag for x in a]
plot.scatter(X,Y, color="blue")
plot.show()

# To rotate a complex number at different degrees
# (a) Rotation by 90 degree:
import matplotlib.pyplot as plt
m=2+4j
n=1j
plt.scatter(m.real,m.imag,color='red')
c=m*n
plt.scatter(c.real,c.imag,color='purple')
plt.show()

# (b) Rotation by 180 degree:
import matplotlib.pyplot as plt
m=2+4j
n=-1
plt.scatter(m.real,m.imag,color='red')
c=m*n
plt.scatter(c.real,c.imag,color='purple')
plt.show()

# (c) Rotation by 270 degree: 
import matplotlib.pyplot as plt
m=2+4j
n=-1j
plt.scatter(m.real,m.imag,color='red')
c=m*n
plt.scatter(c.real,c.imag,color='purple')
plt.show()