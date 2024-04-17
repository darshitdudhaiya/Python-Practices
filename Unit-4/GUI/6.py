from tkinter import *
from tkinter.messagebox import *


mainWindow = Tk()

btn1 = Button(mainWindow, text="Click Here")
btn1.pack(side="top")

def clickHandler(e):
    showinfo("Info title", "Info Message Content")
    showerror("Error title", "Error Message Content")
    showwarning("Warning title", "Warning Message Content")

btn1.bind("<Button-1>", clickHandler)

mainWindow.mainloop()
