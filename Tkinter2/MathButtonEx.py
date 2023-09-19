import tkinter as tk
from tkinter import messagebox
from math import *



def eval_expression(event):
    result.configure(text = " Result: " +
                     str(eval(entry.get())))

    messagebox.showinfo("Evaluate Expression",
                        "Successfully evaluated" )

root = tk.Tk()
root.geometry('300x150+600+200')

root.title('Evaluate Expression')

input_label = tk.Label(root, text = " Enter Your Expression:",).grid(row = 1)
entry = tk.Entry(root)

entry.bind("<Return>", eval_expression)
entry.grid(row=1, column=1)
result= tk.Label(root)
result.grid(row=2,column=1)
result= tk.Label(root)
result.grid(row=2, column=1)
root.mainloop()

