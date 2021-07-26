from tkinter import *
import requests
from PIL import ImageTk,Image
from tqdm import tqdm
import os
import subprocess


app = Tk()
app.title('Save from net')

try:
    app.iconbitmap('./assets/icon.ico')
    background = ImageTk.PhotoImage(Image.open('./assets/background.png'))
    my_background = Label(image=background).pack()
    



except:
    error = Label(text='My assets were not found. Downloading the assets...',fg='red')
    error.pack()
    t_or_f = os.path.isdir('assets')
    if t_or_f == True:
        t_or_fV2 = os.path.isfile('./assets/background.png')
        t_or_fV3 = os.path.isfile('./assets/icon.ico')
        if t_or_fV2 == False or t_or_fV3 == False:
            try:
                subprocess.call('powershell wget "https://www.dropbox.com/s/6tp9y02cngvj9x1/icon.ico?dl=1" -outfile "./assets/icon.ico"',shell=True)
                subprocess.call('powershell wget "https://www.dropbox.com/s/gxjwnq5i1y513t5/background.png?dl=1" -outfile "./assets/background.png"',shell=True)
                error = Label(app,text='Downloaded the required files this relaunch the app to use assets',fg='red')
            except:
                error = Label(app,text='Unable to download file. are you connected to the internet?',fg='red')
                error.pack()


    elif t_or_f == False:
        try:
            os.mkdir('assets')
            t_or_fV2 = os.path.isfile('./assets/background.png')
            t_or_fV3 = os.path.isfile('./assets/icon.ico')
            try:
                subprocess.call('powershell wget "https://www.dropbox.com/s/6tp9y02cngvj9x1/icon.ico?dl=1" -outfile "./assets/icon.ico"',shell=True)
                subprocess.call('powershell wget "https://www.dropbox.com/s/gxjwnq5i1y513t5/background.png?dl=1" -outfile "./assets/background.png"',shell=True)
                error = Label(app,text='Downloaded the required files this relaunch the app to use assets',fg='red')
            except:
                error = Label(app,text='Unable to download file. are you connected to the internet?',fg='red')
                error.pack()
        
        except:
            error = Label(app,text='Not enough perms to make a folder',fg='red')


download_link = Entry(app,width=60,border=5,bg='white',fg='blue')
download_link.pack()
download_link.get()
download_link.insert(0,'Paste the download link here!')


saveas = Entry(app,width=20,border=5,bg='white',fg='green')
saveas.pack()
saveas.get()
saveas.insert(0,'Name of your file')




def download():
    chunk_size = 1000
    
    url = f"{download_link.get()}"
    
    req = requests.get(url, stream = True)
    
    total_size = int(req.headers['content-length'])

    print ("Downloading. Please wait")

    time = 0
    with open(saveas.get(), "wb") as file:
        for data in tqdm(iterable=req.iter_content(chunk_size=chunk_size), total = total_size/chunk_size, unit='KB'):
            file.write(data)
            time+=1
    download_progress = Label(app,text='Download Completed',fg = '#b700ff' , bg='#f7ffb8')
    download_progress.pack()
    # except:

    #     download_progress = Label(app,text='Download failed!',fg = 'green' , bg='white')



download_button = Button(app,text='Start Download',border=5,bg='green',fg='white',command=download)
download_button.pack()



exit_button = Button(app,text='Exit Program', border=5 , bg='#f0443e' , fg='white' ,command=app.quit)
exit_button.pack()





app.mainloop()