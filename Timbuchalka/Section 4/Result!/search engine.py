apps = ["","Task manager" , "Run" , "Windows explorer" , "Start" , "Notepad" , "Minecraft launcher" , "Google Chrome" , "Microsoft edge" , "java" , "Python", "Command prompt" , "cmd", "Opera GX","Opera gx" , "Pip" , "VScode" , "COD", "cod", "Visual studio", "Minecraft"]

item_to_find = None

found = None
prompt = input("Type the name of an app (remember it case sensitive)... we will search in in our database:\t\t")

item_to_find = prompt.capitalize()

if prompt.capitalize() in apps:
    found = apps.index(item_to_find)
#print (prompt.casefold()) this is a test

if found != None:
    print (f"Yay we found your app ({prompt}) in position {found}")
    endkey = input ("Press enter to exit\
	\t\t\t ")
else:
    print(f"Sorry, your app "+(prompt.capitalize())+" is not in our database")
    endkey = input ("Press enter to exit\
	\t\t\t ")
##################################################################################################################