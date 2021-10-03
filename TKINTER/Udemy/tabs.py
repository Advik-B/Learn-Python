from logging import root
from tkinter import *
from tkinter import ttk
from PIL import ImageTk

root = Tk()
root.geometry('650x650+650+200')

icon = ImageTk.PhotoImage(file=r'''C:\Users\advik\Pictures\FRIDAY NIGHT FUNKIN'_files\7429540_large.jpg''')

tabs = ttk.Notebook(root)
tabs.pack(fill=BOTH , expand=True)

tab1=ttk.Frame(tabs)
tab2=ttk.Frame(tabs)

tabs.add(tab1 , text='First Tab')
tabs.add(tab2 , text='Secand Tab' , image=icon )#, compound=LEFT)

tbox = Label(tab2 , text='AD').pack()
# root.resizable(False , False)
root.mainloop()