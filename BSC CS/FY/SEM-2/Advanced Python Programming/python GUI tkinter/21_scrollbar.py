from tkinter import *


root = Tk()
root.geometry("644x333")
root.title("Scrollbar")

# for connecting scrollbar to a widget 
# 1. widget(yscrollcommand = scrollbar.set)
# 2. scrollbar.config(command = Widget.yviews)

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# listbox = Listbox(root, yscrollcommand = scrollbar.set, font="helvetica 16 bold")
# for i in range(344):
#     listbox.insert(END, f"Item {(i)}")

# listbox.pack(fill=BOTH, padx=22, pady=12)

text = Text(root, yscrollcommand = scrollbar.set, font="consolas 11", height=100)
text.pack(fill=BOTH) 

# scrollbar.config(command = listbox.yview)
scrollbar.config(command = text.yview)

Button(root, text="Apply").pack()

root.mainloop()