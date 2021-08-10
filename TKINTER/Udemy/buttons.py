from tkinter import *

root = Tk()

def callback():
    label.config(text='You clicked me!')

label = Label(root , text='Hello Python')
label.pack()

button = Button(root , text='Click Me' ,command=callback)
button.pack()

root.geometry('350x250')
root.mainloop()