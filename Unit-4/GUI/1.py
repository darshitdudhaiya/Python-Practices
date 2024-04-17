from tkinter import *


mainWindow = Tk(screenName="D1")

btn1 = Button(mainWindow, text="BTN-1")
btn1.pack(side=LEFT)
btn2 = Button(mainWindow, text="BTN-2")
btn2.pack(side=RIGHT)
btn3 = Button(mainWindow, text="BTN-3")
btn3.pack(side=TOP)
btn5 = Button(mainWindow, text="BTN-5")
btn5.pack(side=BOTTOM)
btn4 = Button(mainWindow, text="BTN-4")
btn4.pack(side=BOTTOM)

mainWindow.mainloop()
