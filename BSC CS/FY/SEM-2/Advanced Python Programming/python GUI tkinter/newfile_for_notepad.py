def font_window():
    window = Toplevel(root)
    window.geometry("700x600+800+200")
    window.title("Font")
    window.iconbitmap(None)
    window.configure(bg="white")

    # create a font chooser function
    def font_chooser(e):
        our_font.config(family=my_listbox.get(my_listbox.curselection()))

    # create a font_size_chooser function
    def font_size_chooser(e):
        our_font.config(size=font_size_listbox.get(
            font_size_listbox.curselection()))

    # create a font_style_chooser function
    def font_style_chooser(e):
        style = font_style_listbox.get(
            font_style_listbox.curselection()).lower()

        if style == "bold":
            our_font.config(weight=style)

        if style == "regular":
            our_font.config(weight="normal", slant="roman",
                            underline=0, overstrike=0)

        if style == "italic":
            our_font.config(slant="italic")

        if style == "bold/italic":
            our_font.config(weight="bold", slant="italic")

        if style == "underline":
            our_font.config(underline=1)

        if style == "strike":
            our_font.config(overstrike=1)

    # Designate our font
    our_font = font.Font(family="Dubai", size="32")

    # creating Frame
    my_frame = Frame(window, width=600, height=100, background="white")
    my_frame.pack()
    # freeze Frame in place
    my_frame.grid_propagate(False)
    my_frame.columnconfigure(0, weight=10)

    lbl = Label(my_frame, text="Sample text", borderwidth=3,
                relief=FLAT, font=our_font, background="white")
    lbl.grid(row=0, column=0)
    lbl.grid_rowconfigure(0, weight=1)
    lbl.grid_columnconfigure(0, weight=1)

    bottom_frame1 = Frame(
        window, width=800, height=300, background="white")
    bottom_frame1.pack(side=LEFT, padx=15)

    bottom_frame2 = Frame(
        window, width=800, height=300, background="white")
    bottom_frame2.pack(side=LEFT, padx=15)

    bottom_frame3 = Frame(
        window, width=800, height=300, background="white")
    bottom_frame3.pack(side=LEFT, padx=15)

    # Add Labels
    font_label = Label(bottom_frame1, text="Choose Font",
                       font=("Helvetica 14"), background="white")
    font_label.pack(anchor=W)

    size_label = Label(bottom_frame2, text="Font Size",
                       font=("Helvetica 14"), background="white")
    size_label.pack(anchor=W)

    style_label = Label(bottom_frame3, text="Font Style",
                        font=("Helvetica 14"), background="white")
    style_label.pack(anchor=W)

    # Adding Font listbox
    my_listbox = Listbox(bottom_frame1, selectmode=SINGLE, height=19, width=30, font="Helvetica 11", borderwidth=1,
                         relief=SUNKEN)
    my_listbox.pack(side=LEFT)

    # Add Size listbox
    font_size_listbox = Listbox(bottom_frame2, selectmode=SINGLE, height=19, width=15, font="Helvetica 11", borderwidth=1,
                                relief=SUNKEN)
    font_size_listbox.pack(side=LEFT, padx=10)

    # Add style listbox
    font_style_listbox = Listbox(bottom_frame3, selectmode=SINGLE, height=19, width=15, font="Helvetica 11", borderwidth=1,
                                 relief=SUNKEN)
    font_style_listbox.pack(side=LEFT)

    # Add Font Families to listbox
    for f in font.families():
        my_listbox.insert("end", f)

    # Add Font Sizes to listbox
    font_sizes = [8, 10, 12, 14, 16, 18, 20, 22, 24, 26,
                  28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
    for size in font_sizes:
        font_size_listbox.insert("end", size)

    # Add Font Styles to liatbox
    font_styles = ["Regular", "Bold", "Italic",
                   "Bold/Italic", "Underline", "Strike"]
    for style in font_styles:
        font_style_listbox.insert("end", style)

    # Adding scroll bar for fonts
    my_scrollbar = Scrollbar(bottom_frame1, orient=VERTICAL)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    my_scrollbar.config(command=my_listbox.yview)
    my_listbox.config(yscrollcommand=my_scrollbar.set)

    # Adding scroll bar for fonts sizes
    my_scrollbar = Scrollbar(bottom_frame2, orient=VERTICAL)
    my_scrollbar.pack(side=LEFT, fill=Y)
    my_scrollbar.config(command=font_size_listbox.yview)
    font_size_listbox.config(yscrollcommand=my_scrollbar.set)

    # Adding scroll bar for fonts styles
    my_scrollbar = Scrollbar(bottom_frame3, orient=VERTICAL)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    my_scrollbar.config(command=font_style_listbox.yview)
    font_style_listbox.config(yscrollcommand=my_scrollbar.set)

    # Bind The Listbox
    my_listbox.bind("<ButtonRelease-1>", font_chooser)

    # Bind The font_size_listbox
    font_size_listbox.bind("<ButtonRelease-1>", font_size_chooser)

    # Bind The font_style_listbox
    font_style_listbox.bind("<ButtonRelease-1>", font_style_chooser)

    def cancel():
        window.destroy()

    def Apply():
        root.update()

    b1 = Button(window, text="Cancel", command=cancel, anchor=W)
    b1.pack()

    b2 = Button(window, text="Apply", command=Apply, anchor=W)
    b2.pack()
