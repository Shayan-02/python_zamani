from tkinter import *


def show_fullName():
    first = first_entry.get()
    last = last_entry.get()
    fullname = first + " " + last
    show_fullName_label.config(text=fullname)

root = Tk()
root.geometry("500x500")
root.title("fullname app")
root.config(bg = "gray")
root.resizable(0, 0)

first_label = Label(root, text="first name", font=("arial", 14, "bold")).place(x=20, y=20)
last_label = Label(root, text="last name", font=("arial", 14, "bold")).place(x=20, y=60)

first_entry = Entry(root, font=("arial", 14, "bold"), width=20)
first_entry.place(x=150, y=20)
last_entry = Entry(root, font=("arial", 14, "bold"))
last_entry.place(x=150, y=60)

show_fullName_btn = Button(root, text="show fullname", font=("arial", 18, "bold"), command=show_fullName).place(x=80, y=100)


show_fullName_label = Label(root, text="", font=("arial", 14, "bold"))
show_fullName_label.place(x=20, y=150)

root.mainloop()