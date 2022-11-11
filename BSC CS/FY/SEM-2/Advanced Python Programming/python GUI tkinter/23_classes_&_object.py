from distutils.command.upload import upload
from email.policy import strict
from struct import pack
from tkinter import *

from pip import main

# root = Tk()
# root.geometry("644x333")
# root.title("Classes & Objects")

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("644x333")
        self.title("Classes & Objects")

    def status(self):
        self.var = StringVar()
        self.var.set("Busy..")
        self.statusbar = Label(self, textvariable=self.var, relief=SUNKEN, anchor="w", font="Consolas 11")
        self.statusbar.pack(side=BOTTOM, fill=X)

    def click(self):
        print("Button Clicked")
        
    def createbutton(self, inptext):
        Button(text=inptext, command=self.click).pack()

if __name__ == '__main__':
    window = GUI()
    window.status()
    window.createbutton("Dabao button")
    window.mainloop()



# root.mainloop()