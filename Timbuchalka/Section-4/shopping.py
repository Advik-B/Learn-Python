shopping_list = ["Milk" , "pasta" , "spam", "bread" , "rice"]
# for item in shopping_list:

#     if item != "spam":

#         print ("Buy "+item)

for item in shopping_list:
    if item == "spam":
        continue
    print ("Buy "+item)
