# Import necessary libraries
from tkinter import *

# Setting up main Window
root = Tk()
root.geometry("400x300")
root.title("main")

# Function to open New (Top Level) Window
def topwin():
    # Setting up Top Window
    top = Toplevel()
    top.geometry("180x100")
    top.title("toplevel")
    # Adding a label widget to Top Window
    l2 = Label(top, text = "This is a toplevel window")
    l2.pack()

    top.mainloop()

    # Adding a label and button widget to Root (main)window
l = Label(root, text = "this is root window")
btn = Button(root, text = "Click to open annother window", command=topwin)

    # Arranging window
l.pack()
btn.pack()
root.mainloop()