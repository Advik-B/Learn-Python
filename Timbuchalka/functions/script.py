from advik import write as w

from advik import read as r

import time


fpath = ('C:/Users/advik.ADVIK-PC/Documents/THIS IS MADE WITH PYTHON.txt')

w(fpath,
'HELLO WORLD!\n'
'How are you')

print()

print (f'THIS IS THE CONTENT OF "{fpath}"\n'
f"{' '*(len(fpath)+25)}\n"
f"{'↓'*(len(fpath)+25)}")

print()

print(r(fpath)) # Reading the file so that i don`t have open notepad every time
time.sleep(15)