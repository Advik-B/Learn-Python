#                   1
#         01234567890123
parrot = "Norwegian Blue "
print (parrot)
print ()
print (parrot[0:14:2])
number = "9,567,234,123,697,999"
seperators =  number[1::4]
print (seperators)
values = " ".join(char if char not in seperators else " " for char in number).split()
print ([int(val) for val in values])
for Advik in range (99,299):
    print (Advik)
print ("Yay The Code is successful")
endkey = input ("\t------Press 'Enter' to Exit------")
print ("exiting program...")