fruit = {

    "Orange":"A sweet (orange in colour), citrus fruit.",
    "Apple":"Good for shooing the doctors away!",
    "Lemon":"A sour yellow citrus fruit (When life gives you lemons... you make lemonade).",
    "Grape":"A small sweet fruit growing in bunches, has vairus varities!",
    "Lime":"DO NOT MISTAKE THIS FOR A LEMON LIME IS DIFFERENT!!!"
    }

print(fruit)

for f in sorted((fruit.keys())):
    print(f + " - " + fruit[f])

print("\n"*5)

# for val in fruit.values():
#     print(val)

# print('-'*80)

# for key in fruit:
#     print(fruit[key])

# print(fruit.keys())

# print(fruit.values())

# fruit_keys = fruit.keys()
# print(fruit_keys)

# fruit["tomato"] = "Not nice with ice cream. is good with pizza"

# print(fruit_keys)

print(fruit)
print()
print(fruit.items())
f_tuple = tuple(fruit.items())

print()

for snack in f_tuple:
    item, descripition  = snack
    print(item,'-',descripition)

print()
print(dict(f_tuple))