from logging import root
from sqlite3 import Row
from tkinter import *

root = Tk()
root.geometry("655x333")

def getvals():
    print("submitting the form")

    print(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paymentmodevalue.get(), foodservicevalue.get()} ")

    
    with open("records.txt", "a") as f:
        f.write(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paymentmodevalue.get(), foodservicevalue.get()} \n")


# Heading
label = Label(root, text="Welcome to varaliya's Travels", font="comicsansms 13 bold", pady=15).grid(row=0, column=3)

# text for our form
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency Contact")
paymentmode = Label(root, text="Pyment Mode")

# pack text for our form by grid method
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentmode.grid(row=5, column=2)

# Tkinter variable for storing entries
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentmodevalue = StringVar()
foodservicevalue = IntVar()

# Entries for our form
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emergencyentry = Entry(root, textvariable=emergencyvalue)
paymentmodeentry = Entry(root, textvariable=paymentmodevalue)

# packing the entries by grid method
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymentmodeentry.grid(row=5, column=3)

# Checkbox & packing it
foodservice = Checkbutton(text="Want to prebook your meals!", variable=foodservicevalue)
foodservice.grid(row=6, column=3)

# Button & packing it and assigning it a command
Button(text="Submit to Varaliya's Travel", bg="sky blue", fg="black", command=getvals).grid(row=7, column=3)


root.mainloop()