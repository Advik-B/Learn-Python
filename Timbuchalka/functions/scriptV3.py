from advik import write as w

from advik import read as r

import platform as pl
import time
import sys
import getpass


sixtyfour_bit_or_32_bit = (sys.maxsize > 2**32)

tempdat = None

if sixtyfour_bit_or_32_bit == True:
    tempdat = 64
elif sixtyfour_bit_or_32_bit == False:
    tempdat = 32
else:
    pass

username = getpass.getuser()

copyright = (
    "Advik\n", 
    "ADVIK_PC",
)


print (f'You are running on {pl.system()} {pl.release()} {tempdat}-bit.')

print()



print("Type the path of the file to view in plain text mode")

print()

fpath = (input(f"{username.capitalize()}@{pl.system()}-$> "))


print()

print (f'THIS IS THE CONTENT OF "{fpath}"\n'
f"{' '*(len(fpath)+25)}\n"
f"{'↓'*(len(fpath)+25)}")

print()

print(r(fpath)) # Reading the file so that i don`t have open notepad every time
print()
print()
print()
print()
print()
print('Press enter to exit')
input()