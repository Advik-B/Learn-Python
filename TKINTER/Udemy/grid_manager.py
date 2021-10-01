from tkinter import *
from tkinter import ttk

root = Tk()
entry = ttk.Entry(root , width=30)
entry2 = ttk.Entry(root , width=30)
entry.insert(0 , 'Please enter your name')
entry2.insert(0 , 'Please enter your password')

button = ttk.Button(root , text='Enter')
lbltitle = ttk.Label(root , text='Our title here' , font='Helvatica 22')
lblname = ttk.Label(root , text='Your name :')
lblpassword = ttk.Label(root , text='Your password :')

lbltitle.grid( row = 0 , column = 0 , columnspan=2)
lblname.grid(row = 1 , column = 0 , sticky=W)
lblpassword.grid( row = 2  ,column = 0)
entry.grid(row = 1 , column = 1)
entry2.grid( row = 2 , column = 1)
button.grid(row = 3 , column = 1, sticky=E+W , pady=5)

root.geometry('500x400')
root.mainloop()