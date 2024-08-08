# Exercise 2: Library Book Management System
"""
Objective: Develop a Python program to manage a small library's book inventory. This program will involve file handling for storing book information and integrate Python concepts such as functions, input, string manipulation, and try-except blocks, along with data structures like lists and dictionaries.

Problem Statement: Your task is to create a Python program for a library to manage its book inventory. The inventory is stored in a file (library_books.txt), with each line containing a book's title, author, and the number of copies, separated by commas (e.g., "Python Basics, John Doe, 5"). The program should allow adding new books, updating existing book details, displaying all books, and checking the availability of a specific book.

**Instructions:**
1. Read the existing book inventory from "library_books.txt.
2. Provide a menu with options to Add a Book, Update a Book, Display Books, and Check Book Availability.
3. Implement functionalities for each menu option:
    - **Add a Book:** Prompt for book title, author, and number of copies. Add to the inventory if it doesn't exist.
    - **Update a Book:** Allow changing the number of copies of an existing book.
    - **Display Books:** Show all books with their details.
    - **Check Book Availability:** Input a book title and display its availability and author.
4. After each operation, update the 'library_books.txt' file accordingly.
5. Use exception handling to manage file and input errors.
6. Structure your code with appropriate functions for each functionality.

**Hints:**
- Use 'open()' in the appropriate mode to read from and write to the file.
- Consider using 'split()' for string manipulation when reading file lines.
- Store book inventory data in a dictionary for easy access and updates.
- For updating the file, consider writing the entire dictionary back to the file.
- Use relative path 'Module3/Lesson5/Exercise1/filename.txt'
"""

