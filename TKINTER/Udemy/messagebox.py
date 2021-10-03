from tkinter import *
from tkinter import ttk , messagebox

root = Tk()

def callback():
    mbox = messagebox.askquestion('Delete' , 'Are you shure?' , icon='warning')
    if mbox == 'yes':
        print('Deleted')
    else:
        print('Not deleted')

def callback2():
    messagebox.showinfo('Sucess' , 'well done')


button1 = ttk.Button(root , text='Delete' , command=callback)
button1.grid(row=0 , column=0 , pady=25 , padx=50)

button2 = ttk.Button(root , text='Info' , command=callback2)
button2.grid(row=0 , column=1)

root.geometry('350x250')

root.mainloop()