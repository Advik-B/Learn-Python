available_exits = ["North" , "South" ,"East" , "West"]

chosen_exit = ''

while chosen_exit.capitalize() not in available_exits:
    chosen_exit = input("Please choose a direciton:\t\t")
    if chosen_exit.capitalize() == "Quit":
        print ("Game Over")
        break
print ("aren`t you glad you got out of there")
