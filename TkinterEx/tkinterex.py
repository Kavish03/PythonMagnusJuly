from tkinter import *
r = Tk()
frame = Frame(r)
frame.pack()
bottomframe = Frame(r)
bottomframe.pack(side = BOTTOM)
redbutton = Button(frame, text= 'RED', fg='red')
redbutton.pack(side = LEFT)
greenbutton = Button(frame, text ='GREEN', fg='green')
greenbutton.pack(side = LEFT)
bluebutton = Button(frame, text = 'BLUE', fg='blue')
bluebutton.pack(side = LEFT)
brownbutton = Button(frame, text ='BROWN', fg='brown')
brownbutton,pack(side = BOTTOM)
r.mainloop()




r.mainloop()
