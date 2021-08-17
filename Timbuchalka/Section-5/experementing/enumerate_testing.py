letters  = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"

f  = open("Out-Put.txt","w+")

for index,letter in enumerate(letters):
    print (index,"-|-",letter)
    f.write(f'{index} -|- {letter}\n')

# for i in range(0,10000):
#     f.write(f"I am printing for the {i}th time !\n")

f.write("Bye")

f.close