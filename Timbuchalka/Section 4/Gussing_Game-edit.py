import random

highest = 10

answer = int(random.randint(1,highest))

print (answer) #TOD: Remove after testing



print (f"Please guess a number between 1 and {highest}.And type 0 to exit: ")
guess = int(input ())
while guess != answer:
    if guess == 0:
        print("Force Quitting...")
        break
    else:
        if guess != answer:
            if guess < answer:
                print("please guess higher")
            else: #guess must be greater than the answer
                print("please guess lower")
            guess = int(input())
            if guess == answer:
                print ("Well done , you guessed correct")
endkey = input ("Press enter to exit\
	\t\t\t ")