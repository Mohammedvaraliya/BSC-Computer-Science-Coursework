from tkinter import *
from PIL import Image, ImageTk

mahmudul_root = Tk()

mahmudul_root.geometry("655x444")
# photo = PhotoImage(file='1.png')

#below method to display jpg,jpeg, and other etc which was not support in tkinter

image = Image.open("2.jpg")
photo = ImageTk.PhotoImage(image)

label1 = Label(image=photo)
label1.pack()


mahmudul_root.mainloop()