from tkinter import *


mainWindow = Tk()


name = StringVar(mainWindow, "")

lbl1 = Label(mainWindow, text="Enter Name : ")
lbl2 = Label(mainWindow, textvariable=name)
txt1 = Entry(mainWindow, textvariable=name)
btn1 = Button(mainWindow, text="Click Me!")

lbl1.grid(row=0, column=1)
txt1.grid(row=0, column=2)
btn1.grid(row=1, column=0, columnspan=2)
lbl2.grid(row=2, column=0, columnspan=2)

mainWindow.mainloop()

