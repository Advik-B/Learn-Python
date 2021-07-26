Welcome_message = 'Hello World!'

students = [
    "_______\n"
    "Navodit\n",
    "Advik\n",
    "Liaquat\n",
    "Sasank\n", 

]

"""`\n` means next line"""

print(Welcome_message)


"""This will print out the list of students"""
print(students)

print()
"""print () means that it will print a blank line
.... look"""


"""Adding a `*` to a print will unpack it... let me show you."""

print(*students)

"""What if you want to print a welcome message several times???.
then you need to do a for loop. let me show you"""

# for i in range(10):
#     print('Welcome')

"""Here `i` is a varible and in range means the number of times you want to print
your message.

(range(the number of times you want to print the number))"""

'''Now... let us look at the inbuilt functions.
1) print(value) if the value is a word then it should be in '' or "".

2) range(value) if the value is a word then THE PROGRAM WILL CRASH IT SHOULD BE A NUMBER

3) in(value) examples are:
'''

"""it means that if Navo in Navodit = True then print 'Navodit is the best'"""

if "NAVO" in "NAVODIT": 
    """Advik in navodit = False that is why print('navodith was not executed"""
    print('Navodit is the best')