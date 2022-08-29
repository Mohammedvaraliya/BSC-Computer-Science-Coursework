#  WAP to find the product of numbers from 1 to n. (Factorial)

def printFactorial():
    num = int(input("Enter a number : "))

    i = 1
    fact = i

    while(i <= num):
        fact *= i
        i += 1
        
    print(fact)

printFactorial()