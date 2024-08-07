# Exercise 1: E-commerce Product Inventory Management
"""
Objective: To develop a Python program that manages a simple e-commerce platform's product inventory. This program will handle various file operations, including reading, writing, and updating inventory data. It will also integrate key Python concepts such as conditional and loop statements, functions, string manipulation, and exception handling, along with the use of lists, sets, dictionaries, and tuples.

Problem Statement: You are tasked with creating a Python program for managing an e-commerce store's inventory. The inventory data is stored in a text file (inventory.txt), with each line containing a product's name, quantity, and price, separated by commas (e.g., "T-shirt,30, 19.99"). The program should allow adding new products, updating existing product details, displaying all products, and checking stock for a specific product.

**Instructions:**
1. Read the existing inventory data from 'inventory.txt'.
2. Provide a menu with options to Add a Product, Update a Product, Display Inventory, and Check Stock.
3. Implement functionalities for each menu option:
    - **Add a Product:** Prompt for the product name, quantity, and price. Add to inventory if it doesn't exist.
    - **Update a Product:** Allow changing the quantity and price of an existing product.
    - **Display Inventory:** Show all products with their details.
    - **Check Stock:** Input a product name and display its current stock and price.
4. After each operation, update the 'inventory.txt' file accordingly.
5. Use exception handling to manage file and input errors.
6. Structure your code with appropriate functions for each functionality.

**Hints:**
- Use 'open()' in the appropriate mode to read from and write to the file.
- Consider using 'split()' for string manipulation when reading file lines.
- Store inventory data in a dictionary for easy access and updates.
- For updating the file, consider writing the entire dictionary back to the file.

"""

def read_inventory(filename):
    try:
        with open(filename, 'r') as file:
            inventory = {}
            for line in file:
                product, quantity, price = line.strip().split(',')
                inventory[product] = (int(quantity), float(price))
            return inventory
    except FileNotFoundError:
        return {}

def add_product(inventory):
    product = input("Enter product name: ")
    if product in inventory:
        print("Product already exists.")
    else:
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        inventory[product] = (quantity, price)

def update_product(inventory):
    product = input("Enter product name: ")
    if product not in inventory:
        print("Product not found.")
    else:
        quantity = int(input("Enter new quantity: "))
        price = float(input("Enter new price: "))
        inventory[product] = (quantity, price)

def display_inventory(inventory):
    for product, details in inventory.items():
        print(f"{product}: Quantity - {details[0]}, Price - {details[1]}")

def check_stock(inventory):
    product = input("Enter product name to check stock: ")
    if product in inventory:
        print(f"{product}: Quantity - {inventory[product][0]}, Price - {inventory[product][1]}")
    else:
        print("Product not found.")

def write_inventory(filename, inventory):
    with open(filename, 'w') as file:
        for product, details in inventory.items():
            file.write(f"{product},{details[0]},{details[1]}")


def main():
    inventory = read_inventory('Module3/Lesson5/Exercise1/inventory.txt')

    while True:
        print("\n1. Add a product")
        print("2. Update a Product")
        print("3. Display Inventory")
        print("4. Check Stock")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_product(inventory)
        elif choice == '2':
            update_product(inventory)
        elif choice == '3':
            display_inventory(inventory)
        elif choice == '4':
            check_stock(inventory)
        elif choice == '5':
            print ("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")

        write_inventory('Module3/Lesson5/Exercise1/inventory.txt', inventory)

if __name__ == "__main__": # Allows you to run python file using python interpreter
    main()