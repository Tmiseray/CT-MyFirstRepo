"""
Exercise 1: City Library Management System

Instructions:
1. Define a Book Class:
    - Include attributes for title, author, and availability.
    - Define methods for checking out and returning a book, which update the availability status.
2. Create a Library Class:
    - Store a collection of books
    - Include methods to add books, search for a book by title, lend a book, and return a book.
3. Implement User Interaction:
    - Use input functions to allow staff to add, search, lend, and return books.
    - Use loops and conditional statements to handle different user actions.
4. Error Handling:
    - Implement try-except blocks to handle situations like searching for a book that doesn't exist or lending out an already lent out.
5. Data Structures:
    - Use a list to store the collection of Book objects in the Library class.
    - Use a dictionary or a set for efficient searching of books by title.

Explanation:
• The Book class represents individual books with methods to check them out and return them.
• The Library class manages a collection of books. books can be added, searched by title, lent out, and returned.
• The main program loop allows library staff to perform actions based on user input
• Exception handling ensures that the program can gracefully handle unexpected situations.

Hints:
• When a book is checked out or returned, remember to update availability status.
• Consider using a dictionary in the Library class for efficient book search by title.
• Use a loop to continuously allow the user to choose an action until they decide to exit.

"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def check_out(self):
        if self.is_available:
            self.is_available = False
            return True
        return False
    
    def return_book(self):
        self.is_available = True


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def lend_book(self, title):
        book = self.find_book(title)
        if book and book.check_out():
            print(f"Book '{title}' has been lent out.")
        else:
            print(f"Book '{title}' is not available.")
    
    def return_book(self, title):
        book = self.find_book(title)
        if book:
            book.return_book()
            print(f"Book '{title}' has been returned.")
        else:
            print(f"Book '{title}' not found in the library.")


library = Library()

while True:
    action = input("Enter action (add, lend, return, search, exit): ").lower()
    if action == "exit":
        break

    try:
        if action == "add":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(Book(title, author))
            print(f"Added book '{title}'.")
        elif action == "lend":
            title = input("Enter the book title to lend: ")
            library.lend_book(title)
        elif action == "return":
            title = input("Enter the book title to return: ")
            library.return_book(title)
        elif action == "search":
            title = input("Enter book title to search: ")
            book = library.find_book(title)
            if book:
                availability = "available" if book.is_available else "not available"
                print(f"'{title}' by {book.author} is {availability}.")
            else:
                print(f"Book '{title}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

print("Library system closed.")