from tkinter import *


mainWindow = Tk()

btn1 = Button(mainWindow, text="BTN-1")
btn2 = Button(mainWindow, text="BTN-2")
btn3 = Button(mainWindow, text="BTN-3")
btn4 = Button(mainWindow, text="BTN-4")
btn5 = Button(mainWindow, text="BTN-5")

btn1.place(x=0, y=0)
btn2.place(x=100, y=0)
btn3.place(x=100, y=100)
btn4.place(x=0, y=100)
btn5.place(x=50, y=50)

mainWindow.mainloop()
