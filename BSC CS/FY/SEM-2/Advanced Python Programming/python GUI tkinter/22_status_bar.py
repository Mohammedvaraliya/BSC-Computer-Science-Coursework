from cgitb import grey
from distutils.command.upload import upload
from tkinter import *

root = Tk()
root.geometry("644x333")
root.title("Status bar")

def upload():
    statusvar.set("Busy..")
    sbar.update()
    import time
    time.sleep(2)
    statusvar.set("Ready")

statusvar = StringVar()
statusvar.set("Ready")

sbar = Label(root, textvariable=statusvar, relief=GROOVE, fg="black", anchor="w", font="consolas 11")
sbar.pack(side=BOTTOM, fill=X)

Button(root, text="Upload", command=upload, relief=GROOVE).pack()


root.mainloop()