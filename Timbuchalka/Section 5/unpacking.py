from typing import overload


a = b = c = d = e = f = 42
print (c)
 
x, y, z  = 1, 2, 76
print (x)
print (y)
print (z)

print ('Unpacking a tuple')

data = 1, 2, 76
x, y, z = data
print (x)
print (y)
print (z)

print ("Unpacking a list")
data_list =  [ 12 , 13 , 14]

# data_list.append(15)

p , q , r  = data_list

print (p)
print (q)
print (r)

exit("The program finished with exit code 0")