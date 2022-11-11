from cProfile import label
from tkinter import *
from unicodedata import name

root = Tk()
root.geometry("655x333")
root.title("Dance Form")

frame1 = Frame(root, bg="grey", borderwidth=6, relief=GROOVE, padx=23, pady=46)
frame1.pack()

label1 = Label(frame1, text="Dance Academy Form", font="helvetica 19 bold underline", padx=25, pady=4, fg="white",
               bg="black", relief=SUNKEN)

label1.grid(column=1)

name = Label(frame1, text="Name:", bg="grey").grid(row=8, column=0)
DOB = Label(frame1, text="Date Of Birth:", bg="grey").grid(row=9)
age = Label(frame1, text="Age:", bg="grey").grid(row=10)

name = StringVar()
DOB = StringVar()
age = StringVar()

name_entry = Entry(frame1, textvariable=name).grid(row=8, column=1)
DOB_entry = Entry(frame1, textvariable=DOB).grid(row=9, column=1)
age_entry = Entry(frame1, textvariable=age).grid(row=10, column=1)

def save():
    f = open("form.txt", "a")
    f.write(f"Name: {name.get()}\n")
    f.write(f"DOB: {DOB.get()}\n")
    f.write(f"Age: {age.get()}\n\n")
    f.close()
    root.destroy()

Button(frame1, text="Submit", command=save).grid(column=1)




root.mainloop()