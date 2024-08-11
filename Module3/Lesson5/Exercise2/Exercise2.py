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

def read_books(filename):
    try:
        with open(filename, 'r') as file:
            books = {}
            for line in file:
                title, author, copies = line.strip().split(',')
                books[title] = {'author': author, 'copies': copies}
            return books
    except FileNotFoundError:
        return {}

def add_book(books):
    title = input("Enter book title: ")
    if title in books:
        print("Book already exists.")
    else:
        author = input("Enter author's name: ")
        copies = int(input("Enter number of copies: "))
        books[title] = {'author': author, 'copies': copies}

def update_book(books):
    title = input("Enter book title: ")
    if title not in books:
        print("Book not found.")
    else:
        copies = int(input("Enter new number of copies: "))
        books[title]['copies'] = copies

def display_books(books):
    for title, info in books.items():
        print(f"Title: {title}, Author: {info['author']}, Copies: {info['copies']}")

def check_availability(books):
    title = input("Enter book title to check: ")
    if title in books:
        info = books[title]
        print(f"Title: {title}, Author: {info['author']}, Copies: {info['copies']}")
    else:
        print("Book not found.")

def write_books(filename, books):
    with open(filename, 'w') as file:
        for title, info in books.items():
            file.write(f"{title},{info['author']},{info['copies']}\n")


def main():
    books = read_books('Module3/Lesson5/Exercise2/library_books.txt')

    while True:
        print("\n1. Add a book")
        print("2. Update a book")
        print("3. Display books")
        print("4. Check book availability")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_book(books)
        elif choice == '2':
            update_book(books)
        elif choice == '3':
            display_books(books)
        elif choice == '4':
            check_availability(books)
        elif choice == '5':
            print ("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")

        write_books('Module3/Lesson5/Exercise2/library_books.txt', books)

if __name__ == "__main__": # Allows you to run python file using python interpreter
    main()