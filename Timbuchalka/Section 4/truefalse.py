# day = "Friday"
# temprature = 30
# raining = False

# if day == "Saturday" and temprature > 27 or not raining:
#     print ("go swimming")
# else:
#     print ("Learn python")
# f = open("blocks.py" , mode="r" , encoding="utf-8")

# if 0:
#     print ("True")
# else:
#     print ("False")
name = input ("Please Enter your name: ")
#if name:
if name != "":
    print (f"Hello, {name.capitalize()}")
else:
    print ("Are you the person with no name?")