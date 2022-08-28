# WAP to print numbers from 1 to the limit entered by the user, using a while loop.

def printNumbers():
    limit = int(input("Enter the limit : "))
    i = 1

    while i <= limit:
        print(i)
        i += 1

printNumbers()