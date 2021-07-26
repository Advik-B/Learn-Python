import time
import requests
import os
import subprocess


from PIL import ImageTk,Image
from tkinter import *
from google.colab import drive
drive.mount('/gdrive')


app = Tk()
app.title('Python file')
quit_button = Button(app, text='Exit' ,fg='white' , bg="#f0443e", padx=10 ,width=7,command=app.quit)
#if os.path.isdir('assets')
subprocess.call('powershell wget https://www.dropbox.com/s/38vxusmtbxrz9ne/profile%20pic.png?dl=1 -outfile assets/pic.png')

quit_button.pack()
# try:
#     subprocess.call('')
#app.iconbitmap("https://www.dropbox.com/s/38vxusmtbxrz9ne/profile%20pic.png?dl=1")

app.mainloop()