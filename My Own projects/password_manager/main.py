from cryptography.fernet import Fernet
from functions import pinput as pin
import os


def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

if os.path.isfile('./key.key') == False:
    write_key()

def load_key():
    file = open("key.key", "rb")
    key = file.read()   
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def view():
    try:
        with open('password.txt','r') as f:
            for line in f.readlines():
                data = line.rstrip()
                user , passwd = data.split("|")
                print("-"*(len((fer.decrypt(user.encode())).decode().replace("^%^","|"))+10)+"\n"
                    'Username: '+(fer.decrypt(user.encode())).decode().replace("^%^","|")+'\n' 
                    "Password: "+(fer.decrypt(passwd.encode())).decode().replace("^%^","|")+"\n"+
                    ("-"*(len((fer.decrypt(passwd.encode())).decode().replace("^%^","|"))+10)) ,"\n")
    except FileNotFoundError:
        print()
        print('You have no passwords')
        print()

def add():
    name = pin('Account Name:\t')
    if "|" in name:
        name = name.replace("|",'^%^')
    pwd = pin('Account Password:\t')
    if "|" in pwd:
        pwd = pwd.replace("|",'^%^')
    with open('password.txt' , 'a') as f:
        f.write(str(fer.encrypt(name.encode()).decode())+"|"+str(fer.encrypt(pwd.encode()).decode())+"\n")

# pwd = pin('What is the master password')
while True:
    mode = pin('Would you like to add a new password or view existing ones (view/add)?\n'
    '"q" to quit\n')
    if mode.casefold() == 'q':
        break
    if mode.casefold() == 'view':
        view()
    elif mode.casefold() == 'add':
        add()
    else:
        print('Invalid command')
        print()
        continue