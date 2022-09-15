import os

print("File System")
print("\n")
print("1. Create a file")
print("2. Write in a file")
print("3. Append in a file")
print("4. Read from file ")
print("5. Delete a file")
print("\n")

inputNo = int(input("Enter a number : "))

if (inputNo == 1):
    input_fname = str(input("Please give a file name :  "))
    file = open(f"D:\\Practicals Performed\\BSC CS\\SY\\SEM-3\\Operating-Systems\\Practical-10\\Files Folder\\{input_fname}.txt", "a")
    file.close()
    print("File crated successfully.")

elif(inputNo == 2):
    input_fname = str(input("Please provide a file name where you want to write : "))
    input_Str = str(input("Please describe what you write in a file :  "))
    file = open(f"D:\\Practicals Performed\\BSC CS\\SY\\SEM-3\\Operating-Systems\\Practical-10\\Files Folder\\{input_fname}.txt", "w")
    file.write(input_Str)
    file.close()
    print("Successfully written in a file.")


elif(inputNo == 3):
    input_fname = str(input("Please provide a file name where you want to append data : "))
    input_Str = str(input("Please describe what you want to append in a file :  "))
    file = open(f"D:\\Practicals Performed\\BSC CS\\SY\\SEM-3\\Operating-Systems\\Practical-10\\Files Folder\\{input_fname}.txt", "a")
    file.write(input_Str)
    file.close()
    print("Successfully append in a file.")

elif(inputNo == 4):
    input_fname = str(input("Please provide a file name which you want to read : "))
    file = open(f"D:\\Practicals Performed\\BSC CS\\SY\\SEM-3\\Operating-Systems\\Practical-10\\Files Folder\\{input_fname}.txt", "r")
    content = file.readline()
    print(content)
    file.close()
    print("Successfully read the file.")

elif(inputNo == 5):
    inputFile = str(input("Please enter file name which you want to delete : "))
    os.remove(f"D:\\Practicals Performed\\BSC CS\\SY\\SEM-3\\Operating-Systems\\Practical-10\\Files Folder\\{inputFile}.txt")
    print("Successfully deleted the file.")

elif(inputNo > 5):
    print("Please enter a valid input ")