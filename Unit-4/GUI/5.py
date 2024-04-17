from tkinter import *


mainWindow = Tk()

a = StringVar(mainWindow, "")
b = StringVar(mainWindow, "")
c = StringVar(mainWindow, "")

lbl1 = Label(mainWindow, text="Enter A : ")
lbl2 = Label(mainWindow, text="Enter B : ")
lbl3 = Label(mainWindow, textvariable=c)
txt1 = Entry(mainWindow, textvariable=a)
txt2 = Entry(mainWindow, textvariable=b)
btn1 = Button(mainWindow, text="Add")

lbl1.grid(row=0, column=0)
txt1.grid(row=0, column=1)
lbl2.grid(row=1, column=0)
txt2.grid(row=1, column=1)
btn1.grid(row=2, column=0, columnspan=2)
lbl3.grid(row=3, column=0, columnspan=2)

def clickHandler(e):
    a_t = int(a.get())
    b_t = int(b.get())
    c.set(f"{a_t + b_t}")

btn1.bind("<Button-1>", clickHandler)


mainWindow.mainloop()

