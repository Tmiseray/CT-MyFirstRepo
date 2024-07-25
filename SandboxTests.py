shopping_list = []

# Task 1:
def add_item(item):
    global shopping_list
    if item not in shopping_list:
        shopping_list.append(item)
        print(f"\n{item} has been added to your shopping list.")
    else:
        print(f"\n{item} is already on your shopping list.")

# Task 2:
def remove_item(item):
    global shopping_list
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"\n{item} has been removed from your shopping list.")
    else:
        print(f"\n{item} is not currently on your shopping list.")

# Task 3: 
def view_list():
    global shopping_list
    if len(shopping_list) == 0:
        print("\nYour shopping list is empty.")
    else:
        print("\nYour Shopping List:\n")
        for i in range(len(shopping_list)):
            print(f"~ {shopping_list[i]}")

def list_assist():
    while True:
        print("\nShopping List Assistant")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View Shopping List")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            item = input("\nEnter the item to add: ")
            add_item(item.capitalize())
        elif choice == "2":
            item = input("\nEnter the item to remove: ")
            remove_item(item.capitalize())
        elif choice == "3":
            view_list()
        elif choice == "4":
            print("\nList is complete! \nGlad I could assist!")
            break
        else:
            print("\nInvalid choice. Please try again.")

list_assist()