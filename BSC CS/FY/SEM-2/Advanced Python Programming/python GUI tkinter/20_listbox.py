from tkinter import *

root = Tk()
root.geometry("644x333")
root.title("ListBox")

def add():
    global i
    lbx.insert(ACTIVE, f"{i}")
    i+=1
    
i=0
lbx = Listbox(root)
lbx.pack()
lbx.insert(END, "First Item Of Our Listbox")

Button(root, text="Add Item", command=add).pack()

root.mainloop()