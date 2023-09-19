from tkinter import *
Haresh = Tk()
Haresh.geometry('250x250')

def onclick():
    label = Label(Haresh, text ="You have clicked this Button")
    label.pack()

b1 = Button(Haresh, text ="Click this button",command = onclick, fg="red", bg="yellow")
b1.pack()

Haresh.mainloop()

