from tkinter import *

root = Tk()


'''

Creating a label widget

'''
mylabel = Label(root, text= 'Hello World').grid(row=0,column=0)
mylabel2 = Label(root, text= ' My name is Advik').grid(row=1,column=5)

"""
mylabel.grid(row=0,column=0)

mylabel2.grid(row=1,column=5)
"""


#mylabel.pack()

root.mainloop()