from tkinter import *
from tkinter import ttk

root = Tk()
pw = ttk.PanedWindow(root , orient=HORIZONTAL)
pw.pack(fill=BOTH , expand=True)

f1 = ttk.Frame(pw , width=100 , height=500 , relief=SUNKEN)
f2 = ttk.Frame(pw , width=300 , height=500 , relief=SUNKEN)
f3 = ttk.Frame(pw , width=75 , height=500 , relief=SUNKEN)

pw.add(f1 , weight=1)
pw.add(f2 , weight=3)
pw.insert(pos=1 , child=f3)

lbl = Label(f1 , text='hello').pack(pady=25)
bunnton = ttk.Button(f1 , text='Click me!').pack(padx=20 , pady=25)


root.geometry('750x750+650+100')
root.mainloop()
