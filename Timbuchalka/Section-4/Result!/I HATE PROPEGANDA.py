var = None
while True:
    
    var = input("Do you love arnab-GO-swami ? [Y/N] (Press 'Q' to quit)")
    if var not in "" or var != "":
        if var in "n" or var in "N":
            print ("THANK GOD  THAT YOU ARE NOT A VICTIM OF THAT PROPEGANDA")
            endkey = input("Type enter to exit")
            break
        elif var.capitalize() in "Q" or var in "":
            print ("I see that you don`t want to get political. You have made a smart move")
            endkey = input("Type enter to exit")
            break
        elif var.capitalize() in "Y":
            print ("You are stupid, orthodox, and a victim of propeganda!")
            endkey = input("Type enter to exit ")
            break
        else:
            print ("Sorry, invalid input please try again.")
    else:
        print("Sorry, invalid input please try again.")
else:
    print('You are a Hacker of you are seeing this')