from tkinter import *



root = Tk()
root.geometry("500x500")
root.title("calculator")
root.config(bg="gray")
root.resizable(0, 0)

l = Label(root, text="hello", fg="green", bg="white").place(x=150, y=0)
b1 = Button(root, text="click me", fg="green", bg="lightblue").place(x=0, y=0)
b2 = Button(root, text="click me", fg="green", bg="lightblue", width=10, font=("arial", 20, "bold")).place(x=70, y=0)

root.mainloop()