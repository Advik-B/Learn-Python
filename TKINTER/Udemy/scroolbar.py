from tkinter import *
from tkinter import ttk
from halo import Halo
from threading import Thread
from lorem_text import lorem
root = Tk()
root.geometry('700x450')

tBox = Text(root, width=60, height=20, wrap='word', font=['Vendara', 14])
para = []
for i in range(11):
    a = lorem.paragraph()
    para.append(str(a))
    para.append('\n')
tBox.insert('end', *para)
tBox.config(state='disabled')
tBox.grid(row=0, column=0)
scroll = ttk.Scrollbar(root, orient=VERTICAL, command=tBox.yview)
scroll.grid(row=0, column=1, sticky=N+S)
tBox.config(yscrollcommand=scroll.set)
def start():
    spinner = Halo(text='App is running', placement='right', text_color='green' , color='cyan')
    spinner.animation
    t = Thread(target=lambda:spinner.start())
    t.start()
    root.mainloop()
    while True:
        if root.quit:
            spinner.stop()
            exit(0)

start()#14036e5c8bb543e487be3515ecf18642