from tkinter import *
root = Tk()
root.geometry("655x333")

f1 = Frame(root, bg="grey", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill=Y)

l1 = Label(f1, text="Project Tkinter - VS CODE")
l1.pack(pady=142)

f2 = Frame(root, bg="grey", borderwidth=8, relief=SUNKEN)
f2.pack(side=TOP, fill=X)

l2 = Label(f2, text="Welcome to sublime text", font="helvetica 16 bold", fg="red", pady=22)
l2.pack()


root.mainloop()
