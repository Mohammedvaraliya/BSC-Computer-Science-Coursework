from cProfile import label
from tkinter import *

imaginary_tech_root = Tk()

# width x hight
imaginary_tech_root.geometry("644x434")

# Width, height 
imaginary_tech_root.minsize(300, 100)

# width, height
imaginary_tech_root.maxsize(1200, 988)

label1 = Label(text="This is my GUI")
label1.pack()



imaginary_tech_root.mainloop()
