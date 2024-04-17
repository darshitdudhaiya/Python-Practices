from tkinter import *


mainWindow = Tk()
mainWindow.geometry("500x500")

frm1 = Frame(mainWindow, width=100, height=50, bg="orange")
frm1.pack(side="top", fill="y")
frm2 = Frame(mainWindow, width=50, height=50, bg="aqua")
frm2.pack(side="left", fill="x")
frm3 = Frame(mainWindow, width=100, height=50, bg="pink")
frm3.pack(side="right", fill="x")

btn1 = Button(frm1, text="Button-1")
btn1.pack(side="left")
btn2 = Button(frm1, text="Button-2")
btn2.pack(side="right")
btn3 = Button(frm2, text="Button-3")
btn3.pack(side="top")
btn4 = Button(frm3, text="Button-4")
btn4.pack(side="bottom")


mainWindow.mainloop()
