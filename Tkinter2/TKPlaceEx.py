from tkinter import *
Admin = Tk()
Admin.geometry('250x250')

Label(Admin, text ='First Name').place(x=30,y=50)
Label(Admin, text ='Second Name').place(x=20,y=100)
b1= Button(Admin, text='Login').place(x=30,y=150)
e1 = Entry(Admin)
e2 = Entry(Admin)
e1.place(x=100,y=50)
e2.place(x=100,y=100)
Admin.mainloop()
