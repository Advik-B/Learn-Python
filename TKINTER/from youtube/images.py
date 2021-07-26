from tkinter import *
import requests
from PIL import ImageTk,Image
from tqdm import tqdm


root = Tk()
root.title('My app')



try:
    background = ImageTk.PhotoImage(Image.open('C:/Users/advik.ADVIK-PC/Pictures/advik.jpg'))
    my_background = Label(image=background)
    my_background.pack()


    root.iconbitmap('C:/Users/advik.ADVIK-PC/Downloads/favicon (1).ico')

except:
    text = Label(root,text = 'My assets were not found')
    print('My assets were not found')
    text.pack()

button_quit = Button(root, text='Exit Program' ,command=root.quit ,fg='white' ,bg='black', border=5).pack()

button_next = Entry(root , fg='white' , bg='black',border=5)

button_download = Button(root, text = 'Test download',command=None,fg='white',bg='black',border=10).pack()

button_next.pack()

button_next.get()
button_next.insert(0,'https://bit.ly/3jKabcI')




root.mainloop()