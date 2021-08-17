number = (input ("Please enter a series of numbers, using any separators you like:\t\t"))
seperators = ""

for char in number:
    if not char.isnumeric():
        seperators = seperators + char
    else:
        print ()

print (seperators)
values = " ".join(char if char not in seperators else " " for char in number).split()
print (sum([int(val) for val in values]))