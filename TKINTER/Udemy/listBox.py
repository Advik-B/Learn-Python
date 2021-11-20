import os
from tkinter import *
from tkinter import ttk

root = Tk()

sample_list = os.listdir('/')

lBox = Listbox(root , width=40 , height=15 , selectmode=SINGLE)
i = 0
for file in sample_list:
    # print(*file)
    lBox.insert(i , file)
    i += 1

lBox.pack()
root.geometry('650x650+650+200')
root.mainloop()
