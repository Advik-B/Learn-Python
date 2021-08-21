from contents import pantry , recipes
import time
import colorama
colorama.init()
RED = '\u001b[31m'
GREEN = '\u001b[32m'
RESET = '\u001b[0m'
YELLOW = '\u001b[33m'
CYAN = '\u001b[36m'


def add_shopping_item(data: dict, item: str, amount: int) -> None:
    """Add a tuple containing `item` and `amount` to the `data` dict."""
    if item in data:
        data[item] += amount
    else:
        data[item] = amount

display_dict = dict()

for index , key in enumerate(recipes):
    display_dict[str(index + 1)] = key

shopping_list = dict()

while True:
    print('Please choose your recipe')
    print('-------------------------')
    print()
    for key , value in display_dict.items():
        print(f'{key} -- {value}\n')

    choice = input(': ')

    if choice == 0 or choice == '0':
        break
    elif choice in display_dict:
        selected_items = display_dict[choice]

        print(f'You have selected {selected_items}')
        print()
        print('checking ingreidents ...')
        time.sleep(1.5)
        ingreidents = recipes[selected_items]
        print()
        # print(*ingreidents ,sep = ' , ' , end='.\n')
        print()
        for food_item , required_quantity in ingreidents.items():
            quantity_in_pantry = pantry.get(food_item , 0)

            if required_quantity <= quantity_in_pantry:
                print(f'\t{food_item} {GREEN}[ OK ]{RESET}\n')
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                print(f'\t{food_item} {RED}[ NOT FOUND ]{RESET}  \t{YELLOW}{quantity_to_buy} more needed{RESET}\n')
                add_shopping_item(shopping_list, food_item, quantity_to_buy)

print(YELLOW , 'Shopping list:')
for things in shopping_list.items():
    print(CYAN)
    print('\t',*things , sep=' - ')
    print(RESET)

colorama.deinit()
input()