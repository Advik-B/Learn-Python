from tkinter import *




root = Tk()
root.title('My app')
#root.iconbitmap('C:/s/download.ico')

e = Entry(root, width=50,border=6)

e.pack()
e.get()
e.insert(0,'Enter your name')

def myclick():
    myLabel = Label(root,text= e.get())
    myLabel.pack()


myButton = Button(root , text='Enter your Name' , command=myclick)

myButton.pack()

root.mainloop()
input()