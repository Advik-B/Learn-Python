from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Frames')

frame = Frame(root , height=300 , width=300 , bg='cyan' , bd=7 , relief=SUNKEN)
frame.pack(fill=X)

button1 = ttk.Button(frame , text='Button!')
button1.pack()

root.geometry('650x650+450+200')
root.mainloop()
