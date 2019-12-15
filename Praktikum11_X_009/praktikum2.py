from tkinter import Tk, Label, Entry, Button, StringVar
from tkinter import LEFT, RIGHT

my_app = Tk(className = 'Calculator')

L1 = Label(my_app, text = 'Agka 1')
L1.grid(row = 0, column = 0)

str1 = StringVar()
E1 = Entry(my_app, textvariable = str1)
E1.grid(row = 0, column = 1, columnspan = 5)

L2 = Label(my_app, text = 'Angka 2')
L2.grid(row = 1, column = 0)

str2 = StringVar()
E2 = Entry(my_app, textvariable = str2)
E2.grid(row = 1,column =1, columnspan =5)

L3 = Label(my_app, text = 'result')
L3.grid(row = 4, column = 0)

L4 = Label(my_app, text = ' ')
L4.grid(row = 4, column = 1)

def plus():
    a = float(str1.get())
    b = float(str2.get())
    Result = a+b
    L4.config(text = Result)
def minus():
    c = float(str1.get())
    d = float(str2.get())
    Result = c-d
    L4.config(text = Result)
def times():
    e = float(str1.get())
    f = float(str2.get())
    Result = e*f
    L4.config(text = Result)
def devide():
    g = float(str1.get())
    h = float(str2.get())
    Result = g/h
    L4.config(text = Result)

B1 = Button(my_app, text = '+', command = plus).grid(row = 3, column = 0)
B2 = Button(my_app, text = '-', command = minus).grid(row = 3, column = 1)
B3 = Button(my_app, text = 'x', command = times).grid(row = 3, column = 2)
B4 = Button(my_app, text = ':', command = devide).grid(row = 3, column = 3)

my_app.mainloop()
