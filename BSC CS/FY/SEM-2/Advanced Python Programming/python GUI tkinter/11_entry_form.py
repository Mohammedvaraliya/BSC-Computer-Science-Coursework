from tkinter import *

def submit():
    print("Your Form Submmited Successfuly")

root = Tk()
root.geometry("500x333")
root.title("Entry Points")

Label(root, text="Welcome To Your Entery Points", font="comicsansms 15 bold",pady=15, bg="grey", fg="black").grid(row=0, column=3, pady=15)

Label(root, text="Username :", font="Arial 12 bold").grid(row=1, column=2, pady=4, padx=5)
Label(root, text="password :", font="Arial 12 bold").grid(row=2, column=2, pady=4, padx=5)

Entry(root, textvariable=StringVar(), font="comicsansms 12 bold").grid(row=1, column=3, pady=4)
Entry(root, textvariable=StringVar(), font="comicsansms 12 bold").grid(row=2, column=3, pady=4)

Button(root, text="Submit Here", font="comicsansms 13 bold", command=submit, borderwidth=5, relief=SUNKEN, pady=5, bg="blue", fg="white").grid(row=3, column=3, pady=20, padx=1)

root.mainloop()
