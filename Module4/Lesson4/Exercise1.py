"""
Exercise 1. Restaurant Reservation System Refactor

Objective:
To apply clean coding principles and Python OOP concepts to refactor and enhance a basic restaurant reservation system. 
This exercise will focus on improving readability, modularity, and
efficiency of the code.

Problem Statement:
You have inherited a Python script for a restaurant reservation system. The script is functional but poorly organized, with convoluted code and unclear variable names.
Your task is to refactor this script, applying clean coding principles, including clear naming, organizing code into classes and functions, and ensuring efficient
use of data structures.

Script Description:
This script represents a basic reservation system. It uses a dictionary to keep track of reservations for three tables. The functions book_table and cancel_booking allow users to book or cancel reservations, respectively. The main functionoffers a simple text-based interface for interaction. However the script has several limitations in terms of organization, modularity, and error handling, making it a good candidate for refactoring to apply clean coding principles.

Explanation:
- The Restaurant class is responsible for managing reservations. it uses a dictionary for table reservations, allowing for efficient lookups and updates.
- Functions reserve_table and cancel_reservation handle reservation logic, adhering to the single responsibility principle.
- The main function provides an interactive user interface handling inputs and outputs. 
- Error handling to manage user input errors such as invalid table numbers or actions

** Instructions: **
1. Analyze the provided script to identify areas that lack clarity and efficiency. 
2. Rename variables and functions to be descriptive and meaningful.
3. Break down the script into classes and functions, ensuring each has a single responsibility.
4. Use appropriate data structures (lists, sets, dictionaries, tuples) to handle restaurant data effectively.
5. Implement error handling using try-except blocks where necessary.
6. Add input functionality to interact with the user for reservations.
7. (Optional) Incorporate text file handling to store and retrieve reservation data.

Hints:
- Look for long functions that can be broken down into smaller, more focused functions.
- Identify repeated code blocks that can be turned into reusable functions or methods.
- Use dictionaries for storing restaurant tables and reservations for efficient
lookups.
- Utilize lists or sets for handling collections of data like available
menus or customer Information.
- Implement try-except blocks
for handling user input errors or error handling, making it a file handling exceptions.

"""

# Inherited Restaurant Reservation Script

# reservations = {"table1": "", "table2": "", "table3": ""}
# tables = [1, 2, 3]

# def check_table(table_number):
#     if reservations[f"table{table_number}"]:
#         return True
#     return False

# def book_table():
#     table_number = int(input("Enter table number (1-3): "))
#     if table_number not in tables:
#         print("Invalid table number.")
#         return
#     if check_table(table_number):
#         print(f"Sorry, table {table_number} is already booked.")
#     else:
#         name = input("Enter your name for the reservation: ")
#         reservations[f"table{table_number}"] = name
#         print(f"Table {table_number} booked for {name}.")

# def cancel_booking():
#     table_number = int(input("Enter table number (1-3) to cancel booking: "))
#     if table_number not in tables:
#         print("Invalid table number.")
#         return
#     if not check_table(table_number):
#         print(f"No reservation found for table {table_number}.")
#     else:
#         reservations[f"table{table_number}"] = ""
#         print(f"Reservation for table {table_number} canceled.")

# def main():
#     while True:
#         choice = input("Do you want to book or cancel a table? (book/cancel): ")
#         if choice == "book":
#             book_table()
#         elif choice == "cancel":
#             cancel_booking()
#         else:
#             print("Invalid choice. Please type 'book' or 'cancel'.")

# if __name__ == "__main__":
#     main()

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.tables = {1: None, 2: None, 3: None} # Table Number: Reservation Name

    def reserve_table(self, customer_name, table_number):
        if self.tables[table_number] is None:
            self.tables[table_number] = customer_name
            print(f"Table {table_number} reserved for {customer_name}.")
        else:
            print(f"Sorry, table {table_number} is already reserved.")

    def cancel_reservation(self, table_number):
        if self.tables[table_number] is not None:
            reserved_name = self.tables[table_number]
            self.tables[table_number] = None
            print(f"Reservation for {reserved_name} at table {table_number} canceled.")
        else:
            print("There is no reservation for this table.")

def main():
    my_restaurant = Restaurant("Gourmet Python")
    while True:
        try:
            choice = input("Do you want to reserve  or cancel a table? (reserve/cancel): ")
            if choice not in ["reserve", "cancel"]:
                raise ValueError("Invalid choice. Please choose 'reserve' or 'cancel'.")
            table = int(input("Enter table number (1-3): "))
            if choice == "reserve":
                name = input("Enter the name for reservation: ")
                my_restaurant.reserve_table(name, table)
            elif choice == "cancel":
                my_restaurant.cancel_reservation(table)
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()