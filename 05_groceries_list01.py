# This is a grocery list, it asks you which groceries you need and prints it.

grocery_list = []
more_items = True

while more_items:
    grocery_item = input("Which item do you want next? ")
    grocery_list.append(grocery_item)

    keep_adding_items= (input("Do you need more items? y or n:  ")).lower()

    if keep_adding_items!= 'y':
        more_items = False

print(" The items on your grocery list are: ")

for item in grocery_list:
    print(item)
