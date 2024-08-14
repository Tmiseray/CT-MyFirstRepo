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
