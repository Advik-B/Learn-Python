from tkinter import *
from tkinter import ttk

root = Tk()

def callback():
    print('Your name : '+entry.get())
    print('Your password : '+entry2.get())
    if chvar.get() == 1:
        print('"Remember me" is selected')
    else:
        print('not selected')

entry = ttk.Entry(root , width=30)
entry2 = ttk.Entry(root , width=30)
entry.insert(0 , 'Please enter your name')
entry2.insert(0 , 'Please enter your password')
# entry2.config(show = 's')

button = ttk.Button(root , text='Enter')
lbltitle = ttk.Label(root , text='Our title here' , font='Consolas 22')
lblname = ttk.Label(root , text='Your name :')
lblpassword = ttk.Label(root , text='Your password :')

lbltitle.grid( row = 0 , column = 0 , columnspan=2)
lblname.grid(row = 1 , column = 0 , sticky=W)
lblpassword.grid( row = 2  ,column = 0)
entry.grid(row = 1 , column = 1)
entry2.grid( row = 2 , column = 1)
button.grid(row = 3 , column = 1, sticky=E+W , pady=5)

chvar = IntVar()
chvar.set(0)
cbox = Checkbutton(root , text='Remember me!', variable=chvar  , font = 'Arial 16')
cbox.grid(row  = 4 , column = 0 ,sticky=E ,columnspan=2)
button.config(command = callback)

root.geometry('500x400')
root.mainloop()