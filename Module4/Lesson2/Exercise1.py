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