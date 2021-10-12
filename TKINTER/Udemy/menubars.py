from tkinter import *
from tkinter import ttk, messagebox
from halo import Halo
from threading import Thread

def close(app:Tk):
    msg = messagebox.askyesno('Exit App', 'Are you sure you want to quit' , icon='warning')
    if msg:
        app.destroy()
        app.quit()
        

root = Tk()
menu_bar = Menu(root)
root.geometry('800x600+500+150')

file = Menu(menu_bar, tearoff=False)
edit = Menu(menu_bar)
about = Menu(menu_bar)

# Icons
new_ico = PhotoImage(file='icons/new.png')
open_ico = PhotoImage(file='icons/open.png')
exit_ico = PhotoImage(file='icons/exit.png')
save_ico = PhotoImage(file='icons/save.png')

# Menu
file.add_command(label='New', image=new_ico, compound=LEFT)
file.add_separator()
file.add_command(label='Open', image=open_ico, compound=LEFT)
file.add_separator()
file.add_command(label='Save', image=save_ico, compound=LEFT)
file.add_separator()
file.add_command(label='Exit', image=exit_ico, compound=LEFT, command=lambda:close(root))

menu_bar.add_cascade(label='File', menu=file)
root.config(menu=menu_bar)
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