while True:
    choice = input()
    if choice == "0":
        break
    elif choice in "1" or choice in "2" or choice in "3" or choice in "4" or choice in "5":
        print (f"You chose {choice}")
    else:
        print ("Please choose your option from the list below:")
    print ("1:\tLearn Python")
    print ("2:\tLearn Java")
    print ("3:\tGo swimming")
    print ("4:\tHave Dinner")
    print ("5:\tGo to bed")
    print ("0:\tEXIT")
