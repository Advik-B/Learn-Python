from advik import write as w

from advik import read as r

import time

print("Type the path of the file to view in plain text mode")


fpath = (input("---> "))

# w(fpath,
# 'HELLO WORLD!\n'
# 'How are you')

print()

print (f'THIS IS THE CONTENT OF "{fpath}"\n'
f"{' '*(len(fpath)+25)}\n"
f"{'↓'*(len(fpath)+25)}")

print()

print(r(fpath)) # Reading the file so that i don`t have open notepad every time
time.sleep(15)
print()
print()
print()
print()
print()
print('Press enter to exit')
input()