if guess < answer:
    print ("please guess higher")
    guess = int(input())
    if guess == answer:
        print ("well done , you gussed correct")
    else:
        print ("Sorry worng guess")

elif guess > answer:
    print ("please guess lower")
    guess = int(input())
    if guess == answer:
        print ("well done , you gussed correct")
    else:
        print ("sorry , wrong guess. plz restart the program")
else:
    print ("you got it first time")