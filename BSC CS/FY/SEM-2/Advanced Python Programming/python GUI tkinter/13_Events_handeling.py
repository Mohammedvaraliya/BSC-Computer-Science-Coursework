from tkinter import *

root = Tk()
root.title("Events")
root.geometry("644x333")

def varaliya(event):
    print(f"Button Clicked On The Button At {event.x}, {event.y}")

widget = Button(root, text="Click me please")
widget.pack()

widget.bind("<Button-1>", varaliya)
widget.bind("<Double-1>", quit)

root.mainloop()