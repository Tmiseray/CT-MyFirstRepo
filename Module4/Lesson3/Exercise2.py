"""
Exercise 2: Library Management System

Objective:
Develop a library management system that manages book inventory and user checkouts.
This system should handle adding new books, checking books in and out, and tracking user loans.

Problem Statement:
A community library requires a system to keep track of its books and the loans made to library members. 
The system should allow librarians to add new books, check books in and out, and maintain a record of who has borrowed which book.

** Instructions: **
1. Create a Book class with attributes like title, author, ISBN, and availability status.
2. implement encapsulation in the Book class to ensure that direct access to attributes is controlled through getters and setters.
3. Develop a main program that allows librarians to:
    • Add new books to the library.
    • Check out books to users (updating availability status).
    • Check in books from users.
4. Maintain a record (dictionary or list) of all books in the library and their status.
5. Handle input errors or invalid actions using try-except blocks.
6. Utilize a list or set to track users who have currently borrowed books.
7. Optionally, implement text file handling to save and load library data.

Explanation:
This exercise implements a simple library management system. 
The Book class encapsulates details about each book, including its availability. 
The main program offers options to add new books, check them out to users, and check them in when returned. 
The system uses a dictionary to track all books and a separate dictionary to track current loans. 
This exercise demonstrates encapsulation, error handling, and the use of collections (lists/dictionaries) to manage complex relationships in a real-world application.

Hints:
• Use the ISBN as a unique identifier for each book in the library's record-keeping.
• In the main program, use a loop to continually offer options until the librarian chooses to exit.
• For checking books in and out, update the availability status and keep a record of the user who has borrowed the book.

"""

class Book:
    def __init__(self, title, author, isbn):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__is_available = True

    def get_title(self):
        return self.__title
    
    def is_available(self):
        return self.__is_available
    
    def borrow_book(self):
        if self.__is_available:
            self.__is_available = False
            return True
        else:
            return False
        
    def return_book(self):
        self.__is_available = True


def add_book(library):
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    isbn = input("Enter book ISBN: ")
    library[isbn] = Book(title, author, isbn)

def checkout_book(library, current_loans):
    isbn = input("Enter the ISBN of the book to borrow: ")
    user = input("Enter user name: ")
    if isbn in library and library[isbn].borrow_book():
        current_loans[isbn] = user
        print(f"Book '{library[isbn].get_title()}' checked out to {user}.")
    else:
        print("Book not available or not found.")

def checkin_book(library, current_loans):
    isbn = input("Enter ISBN of the book to return: ")
    if isbn in library and isbn in current_loans:
        library[isbn].return_book()
        del current_loans[isbn]
        print(f"Book '{library[isbn].get_title()}' returned.")
    else:
        print("Invalid ISBN or the book was not borrowed.")

def main():
    library = {}
    current_loans = {}
    while True:
        print("\n1. Add Book")
        print("2. Checkout Book")
        print("3. Checkin Book")
        print("4. Exit")
        choice = input("Enter your choice: ")
        try:
            if choice == '1':
                add_book(library)
            elif choice == '2':
                checkout_book(library, current_loans)
            elif choice == '3':
                checkin_book(library, current_loans)
            elif choice == '4':
                break
            else:
                print("Invalid choice.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()