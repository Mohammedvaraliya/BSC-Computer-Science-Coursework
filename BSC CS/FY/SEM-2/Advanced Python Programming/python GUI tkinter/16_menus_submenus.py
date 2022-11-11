from tkinter import *

root = Tk()
root.geometry("644x333")
root.title("VS CODE")

def myfunc():
    print("Your function created successfully")

# use these to create non dropdown menu
# mymenu = Menu(root, )
# mymenu.add_command(label="File", command=myfunc)
# mymenu.add_command(label="Exit", command=quit)
# root.config(menu=mymenu)

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

root.mainloop()