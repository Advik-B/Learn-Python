copyright = ("Advik")
credits= ("TimBuchalka", "Advik" , "Keerti" , "Cookie")

print("Please Enter your name-\t")
name = (input())
if name == int:
    print ("Sorry number {} we don`t accept names like this.")
    endkey = input ("press enter to exit ")
elif name != str:
    print ("Sorry your name contains invalid charecters please try again")
    endkey = input ("Press enter to exit")
