apps = list()
apps = input ("Tell me some apps (seperate the apps by a comma):\t\t")
apps = apps.capitalize()

item_to_find = None

found = None
prompt = input("Type the name of an app (remember it case sensitive)... we will search in in our database:\t\t")

item_to_find = prompt.capitalize()


if prompt.capitalize() in apps:
    found = apps.index(item_to_find)

if found != None:
    prompt = prompt.capitalize
    print (f"Yay we found your app, {prompt} in position {found + 1}")
    endkey = input ("Press enter to exit\
	\t\t\t ")
else:
    print(f"Sorry, your app "+(prompt.capitalize())+" is not in our database")
    endkey = input ("Press enter to exit\
	\t\t\t ")
##################################################################################################################