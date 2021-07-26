low = (1)
high = (1000)
print(f"Please think of a number between {low} and {high}")
input ("Press Enter to start")

gusses = 1
while low != high:
    print(f"\tGussing in the range of {low} and {high}")
    guess = low + (high - low) // 2
    high_low = input("My Guess is {0}. Should I guess higher or lower; Enter"
                    " 'H' for higher and 'L' for lower and 'C' if you think my answer is correct:\t\t "
                        .format(guess)).casefold()
    print("(Press Q to quit the program)")
    if high_low.capitalize() == "H":
        # Guess higher. The low end of the range becomes 1 greater than the guess.
        low = guess + 1
    elif high_low.capitalize() == "L":
        # Guess Lower becomes one less then the guess.
        high = guess - 1
    elif high_low.capitalize() == "C":
        print(f"I got it in {gusses} gusses!")
        endkey = input ("Press enter to exit\
	        \t\t\t ")
        break
    elif high_low.capitalize() == "Q":
        print("Game Over")
        break
    else:
        print ("Invalid input. Please enter H or L or C")
    

    gusses += 1       #gusses = gusses + 1
else:
    print(f"you thinked of the number {low}")

    print (f"I got it in {gusses} gusses")
    endkey = input ("Press enter to exit\
	\t\t\t ")