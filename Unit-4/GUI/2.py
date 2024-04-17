from tkinter import *


mainWindow = Tk()

btn1 = Button(mainWindow, text="BTN-1")
btn2 = Button(mainWindow, text="BTN-2")
btn3 = Button(mainWindow, text="BTN-3")
btn4 = Button(mainWindow, text="BTN-4")
btn5 = Button(mainWindow, text="BTN-5")

btn1.grid(row=0, column=0, ipadx=10, ipady=10, padx=20, pady=20)
btn2.grid(row=0, column=1)
btn3.grid(row=0, column=2)
btn4.grid(row=1, column=0, columnspan=3)
btn5.grid(row=1, column=4)


mainWindow.mainloop()
