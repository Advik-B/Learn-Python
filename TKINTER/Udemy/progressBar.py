from threading import Thread
from tkinter import *
from tkinter import ttk , messagebox

root = Tk()

probar = ttk.Progressbar(root , orient=HORIZONTAL , length=200)
probar.pack(pady=20)
probar.config(mode='indeterminate')
probar.start()
probar.stop()
probar.config(mode='determinate' , maximum=50 ,value=10)
# probar.start()

val=DoubleVar()
val.set(2)

probar.config(variable=val)

scale = ttk.Scale(root , orient=HORIZONTAL , length=200 , var=val , from_=0.0 , to=50)
scale.pack()

def getprogress():
    while True:
        print(val.get())
        if val.get() <= 0:
            messagebox.showinfo('😀' , 'val = 0 so exited!')
            exit(0)

t = Thread(target=getprogress)
t.start() 

probar.start()

root.geometry('550x550+650+250')
root.mainloop()