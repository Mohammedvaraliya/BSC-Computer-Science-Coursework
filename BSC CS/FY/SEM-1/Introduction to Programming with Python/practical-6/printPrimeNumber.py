# WAP to find prime upto n.

def isPrime(num):
    i = 2 
    while i < num:
        if num % i == 0:
            return False

        i += 1

    return True
    

def printPrimeNumber():
    n = int(input("Enter a number: "))
    i = 2

    while i <= n:
        Prime = isPrime(i)

        if      Prime: print(i)
        
        i += 1

if __name__ == "__main__":
    printPrimeNumber()