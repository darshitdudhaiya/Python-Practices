from tkinter import *
from tkinter.simpledialog import *


mainWindow = Tk()

btn1 = Button(mainWindow, text="Click Here")
btn1.pack(side="top")

def clickHandler(e):
    # a = askinteger("Title", "Enter A : ")
    a = askfloat("Title", "Enter A : ")
    # a = askstring("Title", "Enter A : ")
    print(a)

btn1.bind("<Button-1>", clickHandler)

mainWindow.mainloop()
