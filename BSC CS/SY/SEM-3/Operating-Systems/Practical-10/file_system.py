import os

print("File System")
print("\n")
print("1. create a file")
print("2. write in a file")
print("3. Read from file ")
print("4. Delete a file")

a = int(input("Enter a number"))

if (a == 1):
    file = open("C:\\Users\\varal\\Documents\\readme.txt", "a+")
    file.close()
    print("File crated successfully")
elif(a == 2):
    file = open("C:\\Users\\varal\\Documents\\readme.txt", "w+")
    
