from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("644x333")
root.title("Sliders")


def getdollars():
    print(f"Will soon credit {myslider2.get()} dollars to your bank account")
    tmsg.showinfo("Amount Credit", f"Will soon credit {myslider2.get()} dollars to your bank account")


Label(root, text="How Many Dollars Do you Want? : ", font="helvetica 13 bold", borderwidth=6, relief=GROOVE ).grid(row=1, column=2)
myslider2 = Scale(root, from_=0, to=100, orient="horizontal", tickinterval=50, width=100)
myslider2.set(34)
myslider2.grid(row=1, column=3, sticky='we')


Button(root, text="Get Dollars!", pady=10, command=getdollars).grid(row=2, column=3)



root.mainloop()