from tkinter import *



root = Tk()



def myclick():
    myLabel = Label(root,text= 'Look! I clicked a button ')
    myLabel.pack()


myButton = Button(root , text='Click Me' , padx=50 , pady= 50, command=myclick)

myButton.pack()

root.mainloop()