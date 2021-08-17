import random

def get_integer(prompt):
    while True: 
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        print (f'"{temp}" is not a valid number')
        
        
        '''
        else:
            print (f'"{temp}" is not a valid number')
        '''

highest = 1000

answer = int(random.randint(1,highest))

print (answer) #TODO: Remove after testing



print (f"Please guess a number between 1 and {highest}.And type 0 to exit: ")
guess = 0   
while guess != answer:

    guess = get_integer(': ')

    if guess == 0:
        print("Force Quitting...")
        exit()
    else:
        if guess != answer:
            if guess < answer:
                print("please guess higher")
            else: #guess must be greater than the answer
                print("please guess lower")
            guess = int(input())
            if guess == answer:
                print ("Well done , you guessed correct")
                input ("Press enter to exit")


print ("Well done , you guessed correct")
input ("Press enter to exit")