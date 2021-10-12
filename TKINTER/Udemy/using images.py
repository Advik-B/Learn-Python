from tkinter import *
from tkinter import ttk, messagebox
from halo import Halo
from threading import Thread

root = Tk()
root.title('Using Images')
root.geometry('800x600+500+150')

lbl_text = Label(root,
                 text='Using Images',
                 font=['Ubuntu Mono', 20])

logo = PhotoImage(file=r'E:\GitHub-Repos\icons\app-icons\html5-icon.png')
lbl_img = Label(root, image=logo)

# All the packing
lbl_text.pack()
lbl_img.pack(pady=10, padx=10, fill='both')

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