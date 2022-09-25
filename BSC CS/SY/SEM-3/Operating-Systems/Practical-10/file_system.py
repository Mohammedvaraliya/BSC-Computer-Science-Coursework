import os

print("File System")
print("\n")
print("1. create a file")
print("2. write in a file")
print("3. Append in a file")
print("4. Read from file")
print("5. Delete from a file")
print("\n")

current_dir = os.getcwd()
final_dir = os.path.join(current_dir, r"File_System")
if not os.path.exists(final_dir):
    os.mkdir(final_dir)

inputNo = int(input("Enter a number : "))

if(inputNo == 1):
    try:
        input_fname = str(input("Please give a file name : "))
        file = open(f"{final_dir}\\{input_fname}.txt", "x")
        file.close()
        print("file created successfully.")
    except:
        print("Error while creating file")

elif(inputNo == 2):
    try:
        input_fname = str(input("Please provide a file name where you want to write : "))
        content = str(input("Please describe what you want to write in a file : "))
        file = open(f"{final_dir}\\{input_fname}.txt", "w")
        file.write(content)
        file.close()
        print("Successfully written in a file. ")
    except:
        print("Error while writing in a file.")

elif(inputNo == 3):
    try:
        input_fname = str(input("Please provide a file name where you want to append data : "))
        content = str(input("Please describe what you want to append in a file : "))
        file = open(f"{final_dir}\\{input_fname}.txt", "a")
        file.write(content)
        file.close()
        print("Successfully append in a file .")
    except:
        print("Error while appending in a file.")

elif(inputNo == 4):
    try:
        input_fname = str(input("Please provide a file name which you want to read : "))
        file = open(f"{final_dir}\\{input_fname}.txt", "r")
        content = file.read()
        print(content)
        file.close()
        print("Successfully read the file.")
    except:
        print("Error while reading from file.")

elif(inputNo == 5):
    try:
        input_fname = str(input("Please provide a file name which you want to delete : "))
        os.remove(f"{final_dir}\\{input_fname}.txt")
        print("Successfully deleted the file.")
    except:
        print(f"{input_fname} file does not exist.")

elif(inputNo > 5):
    print("please enter a number in range 1 to 5")
    print("Try again")
