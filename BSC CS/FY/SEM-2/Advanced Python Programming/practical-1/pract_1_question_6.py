# WAP to demonstrate working with directories.

import os
print("String format :", os.getcwd())
print("Byte string format :", os.getcwdb())


print("Current directory :", os.getcwd())
# Changing directory
os.chdir('D:\\python Projects\\BSC-CS-Practical-Performed\\BSC CS\\FY\\SEM-2')
print("Current directory :", os.getcwd())

print("The files in CWD are:",os.listdir(os.getcwd()))
print("\n")

# Os.chdir

os.chdir("D:\\python Projects\\BSC-CS-Practical-Performed\\BSC CS\\FY\\SEM-2")

print("Directory changed")
print("\n")

# os.listdir()

path = ("D:\\python Projects\\BSC-CS-Practical-Performed\\BSC CS\\FY\\SEM-2")
dir_list = os.listdir(path)

print("Files and directories in '", path, "' :")

print(dir_list)
print("\n") 

# Scandir()

path = 'D:\\python Projects\\BSC-CS-Practical-Performed\\BSC CS\\FY\\SEM-2'
obj = os.scandir(path)
print("Files and Directories in '% s':" % path)
for entry in obj :
 if entry.is_dir() or entry.is_file():
    print(entry.name)

obj.close() 
