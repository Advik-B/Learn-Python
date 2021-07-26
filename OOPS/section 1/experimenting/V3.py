
import requests
import os
import time
import requests
from zipfile import *
from tqdm import tqdm

path2 = os.getcwd()
directory = "Server"
dirpath2 = os.path.join(path2,directory)
file = "Server.zip"
file_path = os.path.join(dirpath2,file)
file_path2 = os.path.isfile('./Server/Server.zip')
directory2 = os.path.isfile('./Server')

dick=(os.getcwd().replace("\\","/"))
location = (dick+"/Server")
print()
print ("The Minecraft server setup has started.\n",
f"The server will be installed in {location}")
print()

if directory2 == False:
    os.mkdir(dirpath2)
else:
    pass

if file_path2 == False:

    path=(os.getcwd().replace("\\","/"))
    dirpath = (path+"/Server")
    fpath = (dirpath+"/Server.zip")

    chunk_size = 1000
    
    url = "https://www.dropbox.com/s/qa2eobkd7apnb9x/Server.zip?dl=1"
    
    req = requests.get(url, stream = True)
    
    total_size = int(req.headers['content-length'])

    print ("Downloading. Please wait")
    
    with open(fpath, "wb") as file:
        for data in tqdm(iterable=req.iter_content(chunk_size=chunk_size), total = total_size/chunk_size, unit='KB'):
            file.write(data)
    
    print("Download Completed !!!")
else:
    pass

path = os.getcwd()
directory = "Server"
dirpath = os.path.join(path,directory)
file = "Server.zip"
file_path = os.path.join(dirpath,file)

advik = os.path.isfile('./Server/run.bat')

if advik == False:

    with ZipFile(fpath,'r') as zip:
        print ('Extracting server files...')
        time.sleep(0.5)
        zip.printdir()
        zip.extractall(dirpath)
        print("DONE!")
        print()
        print("Install has been successfully completed")
        time.sleep(5)
else:
    print ("The server has already been installed")
    time.sleep(5)
