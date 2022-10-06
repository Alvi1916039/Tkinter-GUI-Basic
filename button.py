# Importing Tkinter
from tkinter import *

root = Tk()

def myclick():
    mylabel = Label(root, text="You have clicked a button!")
    mylabel.pack()
# Creating a label widget
myButton = Button(root, text="Hello TKINTER!", command=myclick)
# Showing it onto screen
myButton.pack()

root.mainloop()
