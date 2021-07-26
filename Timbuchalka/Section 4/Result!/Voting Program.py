name = str(input ("Please enter your name:\t"))
age = int(input ("how old are you, {0} ? ".format(name)))
if age <= 0:
    print ("STOP TRYING TO CONFSE ME.")
    anger = input (f"BYE, {name}  :-( ")
else:
    if age > 100:
        print (" Nice try I AM NOT THAT DUMB")
        endkey = input ("Press enter to exit\
	    \t\t\t ")
    else:
        if age >= 18:
            print ("Hurray you are old enough to vote. Press the 'X' Button on the candidate you want to vote for.")
        else:
            if age < 18:
                print ("Sorry you are not old enough to vote. Please come back {0} years later ".format(18-age))
endkey = input ("Press enter to exit ")
print ("closing program...")