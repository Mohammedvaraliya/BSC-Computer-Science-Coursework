from tkinter import *
from turtle import width

root = Tk()
root.geometry("644x333")
root.title("functions")
root.wm_iconbitmap("1.png")
root.config(background="dark grey")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

print(f"{width}x{height}")

Button(root, text="Close", command=root.destroy, font="helvetica 10 bold", borderwidth=6, relief=GROOVE).pack(pady=100)






root.mainloop()