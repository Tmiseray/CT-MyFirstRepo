"""
Exercise 1: Building a Contact Management System - Instructions

1. Create a Module:
    - Start by creating a Python module (contact_manager. py) that will contain all the functions for the contact management system.
2. Design Functions:
    - Implement the followina functions in vour module:
        - add_contact(contacts, name, phone, email): Adds a new contact to the contacts list.
        - view_contacts(contacts): Displays all the contacts
        - search_contacts(contacts, name): Searches for a contact by name.
        - delete_contact(contacts, name): Deletes a contact by name.
3. Implement Data Structures:
    - Use a list to store all contacts. Each contact should be a dictionary with keys name, phone, and email.
4. User Interface:
    - In your main Python file (main. py), create a user interface using the input function that allows users to choose an action (add, view, search, delete contacts).
5. Error Handling:
    - Include try-except blocks to handle errors, such as searching for a non-existent contact or entering invalid data.
6. Test Your System:
    - Add at least 5 contacts, search for a couple of them, delete one, and view the updated contact list to ensure your system is working correctly.

"""

import contact_manager

def main():
    contacts = []
    while True:
        print("\n1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contacts")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            name = input("Enter Name: ")
            phone = input("Enter Phone: ")
            email = input("Enter Email: ")
            contact_manager.add_contact(contacts, name, phone, email)
        elif choice == '2':
            contact_manager.view_contacts(contacts)
        elif choice == '3':
            name = input("Enter Name to Search: ")
            contact = contact_manager.search_contacts(contacts, name)
            if contact:
                print(f"Contact Found: {contact}")
            else:
                print("Contact not found.")
        elif choice == '4':
            name = input("Enter Name to Delete: ")
            if contact_manager.delete_contact(contacts, name) is not None:
                print("Contact deleted.")
            else:
                print("Contact not found.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()