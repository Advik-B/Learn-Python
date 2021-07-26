name = input("Please enter your name:\t\t")
if name not in "" or name not in " ":
    age = int(input("Please enter your age\t\t"))
    if age < 18 or age > 30:
        print (f"Sorry {name.capitalize()} you are not eligibe for the free vacation")
    else:
        print (f"Yay you can go on a the FREE vacation, Welcome abord, {name.capitalize()}.")
else:
    print ("are you the the person with no name [Y/N]")
    noname = input("")
    if noname == "y" or noname == "Y":
        print ("Sorry we don`t serve people with no names")
    else:
        print ("Please restart the program to try with a name")
