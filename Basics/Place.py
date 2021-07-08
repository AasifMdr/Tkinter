from tkinter import *

root = Tk()
root.geometry("400x250")

name = Label(root, text = "Name").place(x = 30,y = 50)
address = Label(root, text = "Address").place(x = 30,y = 90)
contact = Label(root, text = "Contact").place(x = 30,y = 130)
e1 = Entry(root).place(x = 80, y = 50)
e2 = Entry(root).place(x = 80, y = 90)
e3 = Entry(root).place(x = 80, y = 130)

root.mainloop()