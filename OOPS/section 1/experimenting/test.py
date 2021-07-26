import requests
import os
path=(os.getcwd().replace("\\","/"))
fpath = (path+"/Server.zip")


url = 'https://www.dropbox.com/s/qa2eobkd7apnb9x/Server.zip?dl=1'
 
# download the file contents in binary format
r = requests.get(url)
 
with open(fpath, "wb") as zip:
    zip.write(r.content)