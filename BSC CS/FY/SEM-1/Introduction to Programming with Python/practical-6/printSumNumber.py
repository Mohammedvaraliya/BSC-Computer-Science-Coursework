# WAP to find the sum of numbers from 1 to n.

def printSumNumber():
    n = int(input("Enter the number : "))
    i = 1
    sum = 0

    while(i <= n):
        sum += i
        i += 1

    print(sum)

printSumNumber()