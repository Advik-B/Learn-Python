name = input ("Please enter your name:\t")
age = int(input ("how old are you, {0}? ".format(name)))

if age > 100:
    print ("Nice Try 🙄 ")
else:
    if age < 0:

        print ("I don`t beleve you.... as if your age is in minus (lol)")
    if age >= 18:
        print ("You are old enough vote (yay!) ")
        print("Loading...")
        print ("Please put an 'X' in the box")
    else:
        print ("Please come back in {} years".format( 18 - age ))
endkey = input ("press enter to exit the program\t\t\t\t")
print ("exiting program...")