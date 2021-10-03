from tkinter import *
from tkinter import ttk #, messagebox , filedialog

root = Tk()
root.title('Some App')

title = Label(root , text='Place Geometry' , font=['Vendara' , 15])

name_txt = Label(root , text='Name: ')
Password_txt = Label(root , text='Password: ')

name_input = ttk.Entry(root , width=30)
pass_input = ttk.Entry(root , width=30)

button = ttk.Button(root , text='Save')
button2 = ttk.Button(root , text='Click Me!' ,padding=5).place(relx=.5  , rely=.5 , anchor=CENTER)

#NOTE: Placing
title.place(x=100 , y=20)
name_txt.place(x=20 , y=80)
name_input.place(x=100 , y=80)

Password_txt.place(x=20 , y=110)
pass_input.place(x=100 , y=110)

button.place(x=210 , y=140)

root.geometry('450x450+650+350')
root.mainloop()