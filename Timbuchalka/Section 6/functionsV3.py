def is_palindrome(string):
   '''
   backwards = string[::-1]
   return backwards == string
   '''
   #or
   return string[::-1].casefold() == string.casefold()


def paliindrome_sentence(sentence: str) -> bool:
   """
   `int`
   """
   string = ''

   for char in sentence:
      if char.isalnum():
         string += char
   return string[::-1].casefold() == string.casefold()



# print ('Please enter a word to check-')

# word = input('--->')

# if paliindrome_sentence(word): # if is_palindrone(word) == True:
   
#    print (f'"{word}" is a palindrone.')
# else:
#    print (f'"{word}" is not a palindrone.')

def fibonacci(n:int) -> int:
    """Return the `n`th fibonacci number for positive `n`."""
    if 0 <= n <= 1:
        return n
    n_minus1,n_minus2 = 1,0

    for f in range(n - 1):
        result = None

        result = n_minus2 - n_minus1
        n_minus2 = n_minus1
        n_minus1 = result
    return result

print("\n"*100)

for i in range(36):
    print(i,":",fibonacci(i))