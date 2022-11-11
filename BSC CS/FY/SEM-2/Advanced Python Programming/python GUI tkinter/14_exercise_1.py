from datetime import date, datetime
import imp
from tkinter import *
from typing import final
from PIL import ImageTk, Image 

root = Tk()
root.title("Today's News")
root.geometry("1500x1500")

def every_100(text):
    final_text = ""
    for i in range(0, len(text)):
        final_text +=text[i]
        if i%100==0 and i!=0:
            final_text += "\n"
    return final_text

texts = []
photos = []

for i in range(0, 3):
    with open(f"{i+1}.txt") as f:
        text = f.read()
        texts.append(every_100(text))

        image = Image.open(f"{i+1}.png")
        #TODO: resize these images
        image = image.resize((465, 265), Image.Resampling.LANCZOS)

        photos.append(ImageTk.PhotoImage(image))

f0 = Frame(root, width=800, height=70)
Label(f0, text="Today's News", font="helvetica 33 bold").pack()
f0.pack()
Label(f0, text="May-22-2022", font="helvetica 13 bold").pack()
f0.pack()

f1 = Frame(root, width=900, height=200, padx=32, pady=34)
Label(f1, text=texts[0], font="helvetica 13 bold italic underline", padx=22, pady=42).pack(side="left")
Label(f1, image=photos[0], anchor="e", borderwidth=10, relief="sunken").pack()
f1.pack(anchor="w")

f2 = Frame(root, width=900, height=200, padx=32, pady=34)
Label(f2, text=texts[1], font="helvetica 13 bold italic underline", padx=22, pady=42).pack(side="right")
Label(f2, image=photos[1], anchor="e", borderwidth=10, relief="sunken").pack()
f2.pack(anchor="w")

f3 = Frame(root, width=900, height=200, padx=32, pady=34)
Label(f3, text=texts[2], font="helvetica 13 bold italic underline", padx=22, pady=42).pack(side="left")
Label(f3, image=photos[2], anchor="e", borderwidth=10, relief="sunken").pack()
f3.pack(anchor="w")



root.mainloop()