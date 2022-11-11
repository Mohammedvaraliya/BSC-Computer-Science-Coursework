from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("644x333")
root.title("VS CODE")

def myfunc():
    print("Your function created successfully")

def help():
    print("I will help you maaan")
    tmsg.showinfo("Help", "Varaliya Will Help You Maan")

def rate():
    print("Rate Us")
    a = tmsg.askquestion("Let Us Know😊", "Was Your Experience Good?.. coz you used this GUI!!!!")
    if a == "yes":
        msg = "Great. Please Rate Us On App Store Please"
    else:
        msg = "Tell Us What Went Wrong. We Will Call You Soon"
    tmsg.showinfo("Experience", msg)

def business():
    print("want to get placement in this company")
    ans = tmsg.askretrycancel("Get Mock Placement", "Sorry There Is No Eligibility For Your Preference")
    if ans:
        print("let us know")
    else:
        print("let us know")


mainmenu = Menu(root)
# tearoff argument used when u dont want a line in dropdown
m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="New project", command=myfunc)
m1.add_command(label="Open file", command=myfunc)
m1.add_separator()       
m1.add_command(label="Open folder", command=myfunc)
m1.add_command(label="Save", command=myfunc)
m1.add_command(label="Quit", command=quit)
mainmenu.add_cascade(label="File", menu=m1)
root.config(menu=mainmenu)

m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="Copy", command=myfunc)
m2.add_command(label="Cut", command=myfunc)
m2.add_separator()       
m2.add_command(label="Paste", command=myfunc)
m2.add_command(label="Save", command=myfunc)
m2.add_command(label="Copy all", command=myfunc)
m2.add_command(label="Cut all", command=myfunc)
m2.add_command(label="Quit", command=quit)
mainmenu.add_cascade(label="Edit", menu=m2)
root.config(menu=mainmenu)

sub_menu = Menu(m1, tearoff=0)
sub_menu.add_command(label='Keyboard Shortcuts')
sub_menu.add_command(label='Color Themes')
sub_menu.add_command(label='settings')
m1.add_cascade(label="Preference", menu=sub_menu)

sub_menu = Menu(m2, tearoff=0)
sub_menu.add_command(label='Next_editor')
sub_menu.add_command(label='Previos_editor')
sub_menu.add_command(label='Editor_in_Group')
m2.add_cascade(label="Switch Editor", menu=sub_menu)

m3 = Menu(mainmenu, tearoff=0)
m3.add_command(label="Help", command=help)
m3.add_command(label="Rate Us", command=rate)
m3.add_command(label="Job", command=business)
mainmenu.add_cascade(label="Help", menu=m3)
root.config(menu=mainmenu)


root.mainloop()