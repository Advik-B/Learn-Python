inp = input
p = print 
inp1 = inp("first number\t\t--")
if inp1 >= 100:
    print ("Please try again")
inp2 = inp ("second number\t\t--")
inp3 = inp ("third number\t\t--")
array = [ "\t ", inp1 , inp2 , inp3]
p (array)