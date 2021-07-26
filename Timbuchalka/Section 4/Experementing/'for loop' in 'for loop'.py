print ("first number")
lol = input("--")
print ("second number")
trool = input ("--")
caution = input ("are you shure that u want to break ur PC [Y/N]")
if (('Y') in caution):
    print("ok")
    print("here we go")
    for crash in range (int(lol),int(trool)):
        print (crash)
    print ("press enter to exit the program")
    endkey1 = input ()
elif (('y') in caution):
    print ("ok")
    print ("here we go")
    for crash1 in range (int(lol),int(trool)):
        print (crash1)
    print ("press enter to exit the program")
    endkey2 = input ()
else:
    print ("wise choice ")
    print ("press enter to exit")
    endkey = input ()
