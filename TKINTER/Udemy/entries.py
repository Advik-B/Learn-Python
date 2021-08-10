from tkinter import *
from tkinter import ttk

root = Tk()

def callback():
    val1 = entry.get()
    val2 = entry2.get()

    print('your name is :',val1)
    print('your password is :',val2)

entry = ttk.Entry(root, width=30)
entry.insert(0 , ' Please enter your name')
entry.state(['disabled'])
entry.pack()


entry2 = ttk.Entry(root, width=30)
entry2.config(show='*')
entry2.pack()

button = ttk.Button(root, text='Click Me!' , command=callback)
button.pack()

root.geometry('300x300')
root.mainloop()