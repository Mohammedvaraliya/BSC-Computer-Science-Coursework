# WAP to print a Multiplication table for the number given as input by the user. The user also enters the start and end values for the multiplication table.
def printMultiplicationTable():
    num = int(input("Enter the number  : "))
    start = int(input("Enter the Starting number: "))
    end = int(input("Enter the Ending number: "))

    for number in range(start,end+1):
        print(num," x ", number," = ", num * number)


if __name__ == "__main__":
    printMultiplicationTable()