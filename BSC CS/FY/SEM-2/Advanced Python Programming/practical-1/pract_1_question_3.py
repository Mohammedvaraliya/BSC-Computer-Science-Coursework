# WAP to create file in exclusive mode. Give error message is file does not exist. 

fileName=input("Enter file name: ")
fileName = fileName+".txt"

filel= open(fileName, 'x')
if not filel:
    print("file does not exist!")
else:
    print("File Created")
    print(filel, 'created')

