from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("644x333")
root.title("RadioButton")

def order():
    print("New Order")
    tmsg.showinfo("Order Received", f"we have recieved your order for {var.get()}. Soon u will get your order")

var = StringVar()
var.set("whatever")

Label(root, text="What would you like to have sir?", justify=LEFT, padx=14, font="lucida 23 bold").pack()

radio = Radiobutton(root, text="MenduVada", padx=14, variable=var, value="MenduVada").pack(anchor="w")
radio = Radiobutton(root, text="Idli", padx=14, variable=var, value="Idli").pack(anchor="w")
radio = Radiobutton(root, text="Dosa", padx=14, variable=var, value="Dosa").pack(anchor="w")
radio = Radiobutton(root, text="Paneer Tikka", padx=14, variable=var, value="Paneer Tikka").pack(anchor="w")
radio = Radiobutton(root, text="Sandwitch", padx=14, variable=var, value="Sandwitch").pack(anchor="w")
radio = Radiobutton(root, text="Paneer Masala", padx=14, variable=var, value="Paneer Masala").pack(anchor="w")
radio = Radiobutton(root, text="Masala Dosa", padx=14, variable=var, value="Masala Dosa").pack(anchor="w")

Button(text="Order Now", command=order, borderwidth=6, relief=SUNKEN).pack()

root.mainloop()