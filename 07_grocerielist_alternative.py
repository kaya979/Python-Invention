grocery_list = [] ##All lists follow the same syntax of [ , , ]
needs_items = True ##Do we need items? Yes

while needs_items == True:
    item_to_add = input("What item you want add?  ")
    grocery_list.append(item_to_add)
    print("Your grocery list has the following items:  ")
    print(" ----- ")

    for item in grocery_list:
        print("- " + item )
    print(" ----- ")

    answer = input("Add another item? y/n   ")
    if answer == "n":
        needs_items = False
    
print("Your final grocery list is:   ")
print(" ----- ")
for item in grocery_list: 
    print("  - " + item)

print(" ----- ")


# https://medium.com/thebit/lists-booleans-user-input-how-to-create-a-grocery-list-in-python-44454eba58df