# 1. (1+3j) + (10+20j)
a = 1+3j
b = (10+20j)
print ("Addition of two complex number is :", a+b)


# 2. If x=1+3j then find (x-1)**2
x = 1+3j
y = (x-1)**2
print (y)


# 3. 1+2j*3
x = 1+2j*3
print(x)


# 4. 4*3j**2
x = 4*3j**2
print(x)


# 5. If x=1+3j the find x.real & x.imag
x = 1+3j
print(x.real)
print(x.imag)


# 6. If x=1+3j the find x.conjugate
x = 1+3j
print(x.conjugate())


# 7. Plot S = {3+3i, 4+3i, 2+i, 2.5+i, 3+i, 3.25+i}
import matplotlib.pyplot as plot
x = 2+2j
S = [3+3j, 4+3j, 2+1j, 2.5+1j, 3+1j, 3.25+1j]
X = [x.real for x in S]
Y = [x.imag for x in S]
plot.scatter(X,Y, color="purple")
plot.show()