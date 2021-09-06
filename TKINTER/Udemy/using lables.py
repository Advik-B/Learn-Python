from logging import root
from tkinter import *

root = Tk()
root.geometry('300x250')
label = Label(root , text='Hello Python') # This is the first way
label['text'] = 'This is another way' # This is the second way
label.config(text = 'Hello tkinter') # Yet another way
label.config(font='Times 15' , fg = 'blue') #To change the font and text colour
label.config(warplength='1')
label.pack()
root.mainloop()