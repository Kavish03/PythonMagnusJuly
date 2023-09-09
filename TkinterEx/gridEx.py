from tkinter import *
Admin = Tk()
Admin.geometry('250x250')

Label(Admin, text ='First Name').grid(row=0)
Label(Admin, text ='Second Name').grid(row=1)
e1 = Entry(Admin)
e2 = Entry(Admin)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
Admin.mainloop()

