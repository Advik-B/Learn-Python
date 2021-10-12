from tkinter import *
from tkinter import ttk, messagebox
from halo import Halo
from threading import Thread
from ttkthemes import themed_tk as tk
from time import sleep

root = tk.ThemedTk()
root.geometry('800x600+500+150')
themes = root.get_themes()


def __change_theme():
    while True:
        for theme in themes:
            try:
                root.set_theme(theme)
                lbltheme.config(text=f'Theme: {theme}')
                sleep(3)
            except RuntimeError:
                exit(0)

lbltheme = ttk.Label(root, font=['Vendara', '16'])
btn1 = ttk.Button(root, text='Answer')
btn2 = ttk.Button(root, text='Decline')
btn3 = ttk.Button(root, text='Ignore')
btn4 = ttk.Button(root, text='Block')
btn5 = ttk.Button(root, text='Report')

lbltheme.pack()
btn1.pack(ipady=5, pady=5)
btn2.pack(ipady=5, pady=5)
btn3.pack(ipady=5, pady=5)
btn4.pack(ipady=5, pady=5)
btn5.pack(ipady=5, pady=5)

def start():
    spinner = Halo(text='App is running', placement='right', text_color='green' , color='cyan')
    spinner.animation
    ct = Thread(target=__change_theme)
    ct.start()
    t = Thread(target=lambda:spinner.start())
    t.start()
    root.mainloop()
    while True:
        if root.quit:
            spinner.stop()
            exit(0)

start()