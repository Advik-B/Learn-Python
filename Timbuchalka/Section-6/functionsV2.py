def is_palindrome(string):
   '''
   backwards = string[::-1]
   return backwards == string
   '''
   #or
   return string[::-1].casefold() == string.casefold()


def paliindrome_sentence(sentence):
   string = ''
   for char in sentence:
      if char.isalnum():
         string += char
   return string[::-1].casefold() == string.casefold()



print ('Please enter a word to check-')

word = input('--->')

if paliindrome_sentence(word): # if is_palindrone(word) == True:
   
   print (f'"{word}" is a palindrone.')
else:
   print (f'"{word}" is not a palindrone.')