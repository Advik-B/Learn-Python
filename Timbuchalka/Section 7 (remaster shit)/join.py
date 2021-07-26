myList = [
    
    "a",
    "b",
    "c",
    "d"
]

letters = "abcdefghijklmnopqrstuvwxyz"

def space():
    print()

newString = ''

for c in myList:
    newString += c+', '

# print(type(newString))
print(newString)
space()
print("There is a better way to do this")
space()
newString = ", ".join(myList)

# print(type(newString))
print(newString)
space()
print("Another example is :-")

exit("\n")