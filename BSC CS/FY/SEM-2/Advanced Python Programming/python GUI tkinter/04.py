from ssl import Options
from tarfile import PAX_FIELDS
from textwrap import fill
from tkinter import *
from tkinter.font import BOLD
from turtle import left
root = Tk()
root.geometry("744x433")
root.title("My GUI with varaliya")

# Important Lable Options
# text - adds the text
# bd - background
# fg - foreground
# font - sets the font
# font = ("comicsansms", 19, "bold")
# font = "comicsansms" 19 "bold"
# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE


title_label = Label(text='''Lionel Messi, in full Lionel Andrés Messi, \nalso called Leo Messi, (born June 24, 1987, \nRosario, Argentina), Argentine-born football \n(soccer) player who was named Fédération \nInternationale de Football Association (FIFA) \nworld player of the year six times (2009–12, \n2015, and 2019).''',
        bg = "red", fg = "white", padx = 23, pady = 44, font = ("comicsansms", 19, "bold"), borderwidth = 3, 
        relief = SOLID)

# Important Pack Options
# anchor = nw-north and west
          # ne-north and east
          # sw-south and west
          # se-south and east
# side = top, bottom, left, right
# fill
# padx
# pady

title_label.pack(side = LEFT, anchor = "nw", fill = Y, padx = 34, pady = 34)


root.mainloop()
