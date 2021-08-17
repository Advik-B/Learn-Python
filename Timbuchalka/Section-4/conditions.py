age = int(input("How old are you ?"))

#if age >= 16 and age <= 65:
#if 16 <= age <= 65:
if age in range(16,66):

    print ("Have a good day at work.")

elif age > 100 or age <= 0:

    print ("Nice Try. This program is not dumb.")

    endkey = input ("Press enter to exit")

else:

    print (f"Enjoy your free time, you need to work for us after {65 - age} years.")
print ("-"*80)
