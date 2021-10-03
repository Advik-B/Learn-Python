from tkinter import *
from tkinter import ttk

root = Tk()

def callback():
    result = TextEditor.get(1.0 , END)
    print(result)

TextEditor = Text(root , width=30 , height=10 , font=(('Helvatica') , 15) , wrap=WORD)
TextEditor.grid(row=0 , column=0)

button = ttk.Button(root , text='Save' , command=callback)
button.grid(row=3 , column=0)

root.geometry('550x550')
root.mainloop()