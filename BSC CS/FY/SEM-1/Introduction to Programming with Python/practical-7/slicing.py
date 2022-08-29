# WAP to demonstrate different ways to slice string

def String_Slicing():
    exampleString = "Python is a higher level programming language"
    print("The string is : ", exampleString)

    # Slicing start
    print(exampleString[0:6]) #This will print (python)
    
    print(exampleString[0:18]) #This will print (Python is a higher)

    print(exampleString[19:24]) #This will print (level)

    print(exampleString[25:36]) #This will print (programming)

    print(exampleString[37:]) #This will print (language)

    print(exampleString[:]) #This will print (Python is a higher level programming language)

    print(exampleString[:45]) #This will print (Python is a higher level programming language)


if __name__ == "__main__":
    String_Slicing()