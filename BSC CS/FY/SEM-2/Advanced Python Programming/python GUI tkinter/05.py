from msilib.schema import Font
from tkinter import *
root=Tk()
root.geometry("500x400")
root.title("GUI")
lab=Label(text="Ready",bg="black",fg="white",font=("comicsansms", 19, "bold"),borderwidth=3,relief=SOLID)
lab.pack(side=BOTTOM,anchor="se",fill=X)
lab.pack()
root.mainloop()