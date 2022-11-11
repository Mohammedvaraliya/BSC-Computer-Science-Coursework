from inspect import getargvalues
from tkinter import *
import tkinter

root = Tk()
root.geometry("655x333")

def getvals():
    print(f"The value of user is {uservalue.get()}")
    print(f"The value of password is {passvalue.get()}")

user = Label(root, text="Username")
password = Label(root, text="Password")
user.grid(row=0, column=0)
password.grid(row=1, column=0)

# variable classes in tkinter
# BooleanVar, DoubleVar, IntVar, StringVar

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable=uservalue)
passentry = Entry(root, textvariable=passvalue)

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

Button(text="Submit", command=getvals).grid()


root.mainloop()