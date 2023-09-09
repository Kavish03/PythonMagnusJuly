from tkinter import *
root = Tk()
root.geometry('250x250')

frame = Frame(root)
frame.pack()
bottomframe = Frame(root)
bottomframe.pack(side = BOTTOM)
lb = Button(frame, text= 'LEFT',height=5,width=10, fg='red')
lb.pack(side = LEFT)
rb = Button(frame, text ='RIGHT',height=5,width=10, fg='green')
rb.pack(side = RIGHT)
tb = Button(frame, text = 'TOP',height=5,width=10, fg='blue')
tb.pack(side = TOP)
bb = Button(frame, text ='BOTTOM',height=5,width=10, fg='brown')
bb.pack(side = BOTTOM)
root.mainloop()


