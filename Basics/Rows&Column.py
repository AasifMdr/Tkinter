from tkinter import *

root = Tk()
root.geometry("400x250")

# creating a label widget
myLabel1 = Label(root, text="Tkinter Program Beginning")
myLabel2 = Label(root, text="I am inevitable")
myLabel3 = Label(root, text="I am Iron Man")

# shoving it onto the screen based upon x-axis and y-axis
# that does not move having a constant position
myLabel1.grid(row = 0,column = 0)
myLabel2.grid(row = 2,column = 3)
myLabel3.grid(row = 4,column = 5)

root.mainloop()