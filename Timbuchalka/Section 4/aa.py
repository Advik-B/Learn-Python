x = 23

x += 1
print(x)    # 24

x -= 4
print(x)    # 20

x *= 5
print(x)    # 100

x //= 4
print(x)    # 25

x /= 5
print(x)    # 5.0 - note conversion from int to float

x **= 2
print(x)    # 25.0 - x still represents a float

x %= 5
print(x)    # 0.0 - 25 is exactly divisible by 5

greeting = "Good "

greeting += "morning"
print(greeting)

greeting *= 5
print(greeting)
