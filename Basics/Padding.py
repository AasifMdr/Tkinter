from tkinter import *

root = Tk()
root.geometry("400x250")

# Button without any functions
button1 = Button(root, text = "Click Me")
button1.pack()

# State disabled button
button2 = Button(root, text = "Click", state = DISABLED)
button2.pack()

# Button x and y padding
button3 = Button(root, text = "Click", padx = 50)
button3.pack()
button4 = Button(root, text = "Click", padx = 50, pady = 50)
button4.pack()

root.mainloop()