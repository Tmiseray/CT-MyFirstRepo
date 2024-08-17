"""
Exercise 3. Building an Online Shopping Cart System

Objective:
Develop an online shopping cart system using Python, applying clean coding principles and OOP techniques. 
This exercise will focus on constructing a modular, efficient, and user-friendly shopping cart, incorporating various Python features.

Problem Statement:
Your task is to create a Python-based online shopping cart system for a retail store. The system should allow users to add items to their cart, view the cart, remove items, and check out. 
The system should be designed with clarity, efficiency, and user interaction in mind.

Instructions:
1. Design a class to represent individual items with attributes like name, price, and
category.
2. Create a shopping cart class that can hold multiple items and manage cart operations.
3. Implement functions for adding items to the cart, viewing the cart, removing items, and checking out.
4. Use lists or dictionaries to manage the items in the cart.
5. Implement user input functionality for interacting with the shopping cart system.
6. Apply try-except blocks for handling potential input errors.
7. Modularize the system by separating functionalities into different Python modules.

"""

from cart import ShoppingCart, Item

def main():
    cart = ShoppingCart()
    while True:
        try:
            action = input("Choose action: add, remove, view, checkout: ")
            if action not in ['add', 'remove', 'view', 'checkout']:
                raise ValueError("Invalid action.")
            if action == 'add':
                name = input("Enter item name: ")
                price = float(input("Enter item price: "))
                category = input("Enter item category: ")
                quantity = int(input("Enter quantity: "))
                cart.add_item(Item(name, price, category), quantity)
            elif action == 'remove':
                name = input("Enter item to remove: ")
                cart.remove_item(name)
            elif action == 'view':
                cart.view_cart()
            elif action == 'checkout':
                cart.checkout()
                break
        except ValueError as e:
            print(e)

if __name__ == '__main__':
    main()