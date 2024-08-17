"""
Exercise 2. Refining a Library Management System

Objective:
To apply clean coding principles and Python OOP techniques in restructuring and enhancing a basic library management system.
This exercise will focus on improving code clarity, efficiency, and organization, utilizing various Python constructs.

Problem Statement:
You are provided with a rudimentary Python script for managing a small library. 
The script, while functional, suffers from poor organization, unclear variable names, and lack of modularity.
Your task is to refactor the script to make it more readable, efficient, and maintainable, adhering to clean coding practices.

Instructions:

1. Examine the provided script to identify areas that can be improved for better readability and structure.
2. Rename variables and functions to be more descriptive and meaningful.
3. Reorganize the script into classes and functions with clear, single responsibilities.
4. Utilize appropriate data structures (lists, sets, dictionaries, tuples) for efficient data management.
5. Implement error handling using try-except blocks for robustness.
6. Use input functions to interact with the user for managing library operations.
7. Optionally, integrate text file handling for persistent data storage.

"""

# books = {"book1": 3, "book2": 2, "book3": 0}
# book_names = {"book1": "1984", "book2": "To Kill a Mockingbird", "book3": "The GreatGatsby"}

# def add(b):
#     if b in books:
#         books[b] += 1
#     else:
#         books[b] = 1
#     print(f"Book added: {b}")

# def borrow(b):
#     if books[b] > 0:
#         books[b] -= 1
#         print(f"You have borrowed {b}")
#     else:
#         print("Book not available")

# def main():
#     while True:
#         action = input("Enter 'A' to add a book or 'B' to borrow a book: ")
#         if action == 'A':
#             book_id = input("Enter the book ID to add: ")
#             add(book_id)
#         elif action == 'B':
#             book_id = input("Enter the book ID to borrow: ")
#             borrow(book_id)
#         else:
#             print("Invalid action")

# if __name__ == '__main__':
#     main()


# Refactored!

class Library:
    def __init__(self):
        self.books = {"1984": 5, "To Kill a Mockingbird": 4} # Book title: Quantity

    def add_book(self, title):
        if title in self.books:
            self.books[title] += 1
        else:
            self.books[title] = 1
        print(f"Added {title} to the library.")

    def borrow_book(self, title):
        if self.books.get(title, 0) > 0:
            self.books[title] -= 1
            print(f"You have borrowed {title}.")
        else:
            print(f"Sorry, {title} is not available.")

def main():
    my_library = Library()
    while True:
        try:
            action = input("Enter 'add' to add a book, or 'borrow' to borrow a book: ")
            if action not in ['add', 'borrow']:
                raise ValueError("Invalid action. Please choose 'add' or 'borrow'.")
            book_title = input("Enter the book title: ")
            if action == 'add':
                my_library.add_book(book_title)
            elif action == 'borrow':
                my_library.borrow_book(book_title)
        except ValueError as e:
            print(e)

if __name__ == '__main__':
    main()