# answer = 5

# print ("Please guess a number between 1 and 10: ")
# guess = int(input ())

# if guess != answer:
#     if guess < answer:
#         print("please guess higher")
#     else: #guess must be greater than the answer
#         print("please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print ("Well done , you guessed correct")
#     else:
#         print ("Sorry, you have not guessed correctly")
# else:
#     print ("Yay, you got it first time.")
#      ^^^^^^^^^^^^^^^^^^^^^^
# thease |||||||||||||||||||||| are  the origanal lines of code
answer = 5

print ("Please guess a number between 1 and 10: ")
guess = int(input ())

if guess == answer:
    print ("Yay, you got it first time.")
else:
    if guess < answer:
        print("please guess higher")
    else: #guess must be greater than the answer
        print("please guess lower")
    guess = int(input())
    if guess == answer:
        print ("Well done , you guessed correct")
    else:
        print ("Sorry, you have not guessed correctly")
        print ("To try again, reopen the program")