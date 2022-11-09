# WAP to create file and write data in the file 

FN1 = input("enter the file name >>>")
FN1 = FN1 + '.txt'
F2 = open(FN1, 'w')
F2.write("name , rollno\n")
F2.write("amaan , f101\n")
F2.write("taukeer , f084\n")
F2.write("varaliya , f115\n")
F2.write("nabil , f091\n")
print("filecreated")
print(F2, 'created') 