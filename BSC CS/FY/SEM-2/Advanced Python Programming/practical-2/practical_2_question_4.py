# WAP to demonstrate try-except-else-finally

try:
    n1 = int(input("Enter a number: "))
    n2 = int(input("Enter another number: "))
    a = n1 + n2
except:
    print("Something went wrong")
else:
    print("Result of Added two numbers is : ", a)
finally:
    print("Exiting...")