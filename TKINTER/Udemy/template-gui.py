from tkinter import *
from tkinter import ttk, messagebox
from halo import Halo
from threading import Thread

root = Tk()
root.geometry('800x600+500+150')

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