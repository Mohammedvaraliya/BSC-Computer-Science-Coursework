from tkinter import *
from turtle import width

root = Tk()
root.title("My GUI")

canvas_width = 800
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")
can_widget = Canvas(root, width=canvas_width, height=canvas_height)
can_widget.pack()

# The line goes from the point x1,y1 and x2,y2
can_widget.create_line(0, 0, 800, 400, fill="dark red")
can_widget.create_line(0, 400, 800, 0, fill="dark red")

# To define rectangle so here x1,y1 is (Top left) and x2,y2 is (Bottom right) 
can_widget.create_rectangle(200, 100, 600, 300, fill="purple")

can_widget.create_oval(200, 300, 600, 100, fill="yellow")

# Text will right in such a way that (width and height)
can_widget.create_text(400, 200, text="Python GUI")

root.mainloop()