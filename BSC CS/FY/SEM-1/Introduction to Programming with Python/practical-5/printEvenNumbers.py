# WAP to print even numbers up to the limit given as input by the user.
def printEvenNumber():
    start = int(input("Enter the starting point: "))
    end = int(input("Enter the ending point: "))


    for num in range(start , end +1):
        #Check if the number is divisible by 2 
        if num % 2 == 0:
            print(num)


if __name__ == "__main__":
    printEvenNumber()