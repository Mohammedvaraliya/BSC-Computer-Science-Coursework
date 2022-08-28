# WAP to input a word from the user and print the characters of the word.
def printWordChar():
    name = input("Enter Your Name : ")

    for char in name:
        print(char)

if __name__ == "__main__":
    printWordChar()

# If you want to take a string from userinput so no need to write str