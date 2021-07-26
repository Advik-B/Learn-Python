def is_palindrome(string):
   '''
   backwards = string[::-1]
   return backwards == string
   '''
   #or
   return string[::-1].casefold() == string.casefold()









print ('Please enter a word to check-')
word = input('--->')

if is_palindrome(word): # if is_palindrone(word) == True:
   print (f'"{word}" is a palindrone.')
else:
   print (f'"{word}" is not a palindrone.')
for temp,dds in enumerate(word):
   del temp
   print (dds)