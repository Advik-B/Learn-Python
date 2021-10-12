from tkinter import *
from tkinter import ttk, messagebox
from halo import Halo
from threading import Thread

root = Tk()
root.geometry('800x600+500+150')

title = ttk.Label(root, text='Tree View', padding=10 , font=['Vendara', 25])
def callback(event):
    item=treeview.identify('item', event.x, event.y)
    print(f'You clicked on {treeview.item(item, "text")}')
    
treeview = ttk.Treeview(root)
title.pack(pady=10 ,ipady=10)
treeview.pack()

treeview.insert('', '0', 'item-1', text='First Item')
treeview.insert('', '1', 'item-2', text='Second Item')
treeview.insert('', '2', 'item-3', text='Third Item')
treeview.insert('', '3', 'item-4', text='Forth Item')
treeview.move('item-3', 'item-1', 'end')
treeview.bind('<Double-1>', callback)

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

start()