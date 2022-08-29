# WAP to find fibonacci series upto n.

def printFibonacciSeries():
    num = int(input("Enter the nth number : "))

    a = 0
    b = 1
    sum = 0
    print("Fibonacci Series : ", end=" ")
    while(sum <= num):
        print(sum, end=" ")
        a = b
        b = sum
        sum = b + a

printFibonacciSeries()