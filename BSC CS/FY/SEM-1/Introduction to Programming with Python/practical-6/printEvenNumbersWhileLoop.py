# WAP to print even numbers from start to the limit entered by the user, using a while loop.

def printEvenNumbersWhileLoop():
    start = int(input("Enter the starting point : "))
    limit = int(input("Enter a limit:"))
    
    i = start
    while i <= limit:
        if i % 2 == 0: 
            print(i)
        i+=1


printEvenNumbersWhileLoop()