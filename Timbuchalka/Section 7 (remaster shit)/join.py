myList = [
    "a",
    "b",
    "c",
    "d"
]

newString = ''

for c in myList:
    newString += c+', '

# print(type(newString))
print(newString)
print()
print("There is a better way to do this")
print()
newString = ", ".join(myList)

# print(type(newString))
print(newString)