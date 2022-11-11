from logging import root
from tkinter import *

root = Tk()
root.geometry("655x444")
root.title("GUI BUTTONS")

def hello():
    print("Hello user")

def name():
    print("Name is Varaliya Mohammed")

def work():
    print("My work to explore more and more knowledge from harry")

def occupation():
    print("I am a student of computer science")

frame = Frame(root, borderwidth=6, bg="grey", relief=SUNKEN)
frame.pack(side=LEFT, anchor="nw")

b1 = Button(frame, fg="black", text="Hello", command=hello)
b1.pack(side=LEFT, padx=23)

b2 = Button(frame, fg="black", text="Name", command=name)
b2.pack(side=LEFT, padx=23)

b3 = Button(frame, fg="black", text="Work", command=work)
b3.pack(side=LEFT, padx=23)

b4 = Button(frame, fg="black", text="Ocuupation", command=occupation)
b4.pack(side=LEFT, padx=23)

root.mainloop()