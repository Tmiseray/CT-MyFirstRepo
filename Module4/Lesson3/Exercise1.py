"""
Exercise 1: Inventory Management System

Objective:
Create an inventory management system for a retail store. 
This system will track products, manage stock levels, and handle sales transactions.

Problem Statement:
A small retail store needs a simple inventory management system to keep track of its products, manage stock levels, and process sales. 
The system should allow adding new products, updating stock levels, and handling sales transactions, including
generating receipts.

** Instructions: **
1. Create a Product class to represent individual products. Each product should have attributes like productID, name, price, and quantity.
2. Implement encapsulation in the Product class, ensuring that direct access to attributes is restricted and managed through getters and setters.
3. Develop a main program that allows users to:
    - Add new products to the inventory.
    - Update stock levels for existing products.
    - Process sales transactions, updating stock levels, and printing a sales receipt.
4. Handle incorrect inputs or actions gracefully using try-except blocks.
5. Store the inventory as a list of Product objects.
6. Optionally, use a text file to load initial inventory data and save changes.

Explanation:
This program implements a basic inventory management system.
The Product class encapsulates product-related data and operations. 
Users can add products, update stock levels, and process sales, with the system automatically adjusting inventory and providing transaction receipts. 
The program demonstrates the principles of encapsulation, along with the use of lists, dictionaries, and basic error handling to create a user-friendly, robust system.

Hints:
• Use a dictionary to map product IDs to Product objects for easy retrieval
• For sales transactions, loop through the list of Product objects to update stock levels and calculate total sales.
• Consider using a while loop for the main program to continuously offer options until the user decides to exit.
• Use try-except blocks to catch and handle exceptions like invalid inputs or operations on non-existent products.

"""

class Product:
    def __init__(self, product_id, name, price, quantity):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    def get_productID(self):
        return self.__product_id
    
    def set_productID(self, product_id):
        self.__product_id = product_id
    
    def get_name(self):
        return self.__name
    
    def set_name(self, product_name):
        self.__name = product_name

    def get_price(self):
        return self.__price
    
    def set_price(self, product_price):
        self.__price = product_price

    def get_quantity(self):
        return self.__quantity
    
    def set_quantity(self, product_quantity):
        self.__quantity = product_quantity

def add_product(inventory):
    product_id = input("Enter product ID: ")
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))
    inventory[product_id] = Product(product_id, name, price, quantity)

def update_stock(inventory):
    product_id = input("Enter product ID to update: ")
    if product_id in inventory:
        new_quantity = int(input("Enter new quantity: "))
        inventory[product_id].set_quantity(new_quantity)
    else:
        print("Product not found.")

def process_sale(inventory):
    product_id = input("Enter product ID for sale: ")
    quantity_sold = int(input("Enter quantity sold: "))
    if product_id in inventory and inventory[product_id].get_quantity() >= quantity_sold:
        product = inventory[product_id]
        product.set_quantity(product.get_quantity() - quantity_sold)
        total_price = quantity_sold * product.get_price()
        print(f"Receipt: Sold {quantity_sold} of {product.get_name()} for $ {total_price}")
    else:
        print("Product not found or insufficient quantity")


def main():
    inventory = {}
    while True:
        print("\n1. Add Product")
        print("2. Update Stock")
        print("3. Process Sale")
        print("4. Exit")
        choice = input("Enter your choice: ")
        try:
            if choice == '1':
                add_product(inventory)
            elif choice == '2':
                update_stock(inventory)
            elif choice == '3':
                process_sale(inventory)
            elif choice == '4':
                break
            else:
                print("Invalid choice.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()