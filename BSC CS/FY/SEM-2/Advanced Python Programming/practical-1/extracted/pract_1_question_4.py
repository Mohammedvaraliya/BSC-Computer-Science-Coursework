# WAP to demonstrate the seek() and tell() methods.

f = open("D:\\python Projects\\BSC-CS-Practical-Performed\\BSC CS\\FY\SEM-2\\Advanced Python Programming\\practical-1\\hello.txt", "r")
print(f.tell())

f = open("D:\\python Projects\\BSC-CS-Practical-Performed\\BSC CS\\FY\SEM-2\\Advanced Python Programming\\practical-1\\hello.txt", "r")
print(f.readline())
print(f.tell())

f = open("D:\\python Projects\\BSC-CS-Practical-Performed\\BSC CS\\FY\SEM-2\\Advanced Python Programming\\practical-1\\hello.txt", "r")
f.seek(20)
print(f.tell())
print(f.readline())
f.close()