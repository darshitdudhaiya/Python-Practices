from tkinter import *
from tkinter.messagebox import *


mainWindow = Tk()

btn1 = Button(mainWindow, text="Click Here")
btn1.pack(side="top")

def clickHandler(e):
    # print(askokcancel("Title", "Content"))
    # print(askretrycancel("Title", "Content"))
    # print(askyesno("Title", "Content"))
    print(askyesnocancel("Title", "Content"))

btn1.bind("<Button-1>", clickHandler)

mainWindow.mainloop()
