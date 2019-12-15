from tkinter import Tk, Label, Entry, Button, StringVar
from tkinter import LEFT, RIGHT

my_app = Tk(className = 'Geometri')

L1 = Label(my_app, text = 'Nama Bangunan')
L1.grid(row = 0, column = 0)

str1 = StringVar(value = 'Prisma Segiempat')
E1 = Entry(my_app, textvariable = str1)
E1.grid(row = 0, column = 2)

L2 = Label(my_app, text = ':')
L2.grid(row = 0, column = 1)

L3 = Label(my_app, text = 'Dimensi Bangunan')
L3.grid(row = 1, column = 0)

str3 = StringVar(value = 'Prisma')
E3 = Entry(my_app, textvariable = str3)
E3.grid(row = 1,column =2)

L4 = Label(my_app, text = ':')
L4.grid(row = 1, column = 1)

L5 = Label(my_app, text = 'Contoh Benda')
L5.grid(row = 2, column = 0)

str5 = StringVar(value = 'Atap rumah')
E5 = Entry(my_app, textvariable = str5)
E5.grid(row = 2, column = 2)

L6 = Label(my_app, text = ':')
L6.grid(row = 2, column = 1)

L7 = Label(my_app, text = 'Parameter Panjang')
L7.grid(row = 4, column = 0)

str7 = StringVar(value = ' ')
E7 = Entry(my_app, textvariable = str7)
E7.grid(row = 4, column = 2)

L8 = Label(my_app, text = ':')
L8.grid(row = 4, column = 1)

L9 = Label(my_app, text = 'Parameter Lebar')
L9.grid(row = 5, column = 0)

str9 = StringVar(value = ' ')
E9 = Entry(my_app, textvariable = str9)
E9.grid(row = 5, column = 2)

L10 = Label(my_app, text = ':')
L10.grid(row = 5, column = 1)

L11 = Label(my_app, text = 'Parameter Tinggi')
L11.grid(row = 6, column = 0)

str11 = StringVar(value = ' ')
E11 = Entry(my_app, textvariable = str11)
E11.grid(row = 6, column = 2)

L12 = Label(my_app, text = ':')
L12.grid(row = 6, column = 1)

L13 = Label(my_app, text = 'Result')
L13.grid(row = 8, column = 0)

L14 = Label(my_app, text = ':')
L14.grid(row = 8, column = 1)

L15 = Label(my_app, text = ' ')
L15.grid(row = 8, column = 2)

def hitung():
    a = float(str7.get())
    b = float(str9.get())
    c = float(str11.get())
    result = (a*b*c)
    L15.config(text = result)

B1 = Button(my_app, text = 'hitung', command = hitung)
B1.grid(row = 7, column = 0)

my_app.mainloop()



