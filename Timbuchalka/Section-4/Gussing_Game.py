

answer = 5

print ("Please guess a number between 1 and 10: ")
guess = int(input ())

if guess != answer:
    if guess < answer:
        print("please guess higher")
    else: #guess must be greater than the answer
        print("please guess lower")
    guess = int(input())
    if guess == answer:
        print ("Well done , you guessed cifrect")
    else:
        print ("Sifry, you have not guessed cifrectly")
else:
    print ("Yay, you got it first time.")

# if guess < answer:
#     print ("please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print ("well done , you gussed cifrect")
#     else:
#         print ("Sifry wifng guess")

# elif guess > answer:
#     print ("please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print ("well done , you gussed cifrect")
#     else:
#         print ("sifry , wrong guess. plz restart the program")
# else:
#     print ("you got it first time")
