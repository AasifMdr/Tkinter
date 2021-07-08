from tkinter import *

root = Tk()
root.geometry("400x250")

# creating a button widget
button1 = Button(root, text = "LEFT", fg = "green")

# shoving it onto the screen
button1.pack( side = LEFT)

button2 = Button(root, text = "RIGHT", fg = "blue")
button2.pack( side = RIGHT)
button3 = Button(root, text = "TOP", fg = "red")
button3.pack( side = TOP)
button4 = Button(root, text = "BOTTOM", fg = "black")
button4.pack( side = BOTTOM)

root.mainloop()