# Exercise 7: Daily Task Scheduler
"""
Objective: Create a Python program to manage and schedule daily tasks, integrating file handling for storing task data. This exercise will cover Python concepts such as functions, input handling, string manipulation, conditional and loop statements, and data structures like lists and dictionaries, along with date and time manipulation.

Problem Statement: Develop a Python program to help users organize their daily tasks.
The tasks will be stored in a file (daily_tasks.txt), with each line containing a task description, due date (in YYYY-MM-DD format), and status (e.g., "Finish Python assignment,2023-03-25,Pending"). The program should allow users to mark tasks as completed, view overdue tasks, and display tasks for a specific date.

**Instructions:**
1. Read the existing tasks from 'daily_tasks.txt'.
2. Provide a menu with options to Add New Task, Mark Task as Completed, View Overdue Tasks, and Display Tasks by Date.
3. Implement functionalities for each menu option:
    - **Add New Task:** Allow users to add a task with the format "Finish Python assignment,2023-03-25,Pending"
    - **Mark Task as Completed:** Allow users to select a task and update its status to 'Completed'.
    - **View Overdue Tasks:** Display tasks that are past their due date and still pending.
    - **Display Tasks by Date:** Input a specific date and display all tasks for that date.
4. After updating a task's status, rewrite the 'daily_tasks.txt' file.
5. Use exception handling for potential file reading and writing errors.
6. Structure the code with functions for each task.

**Hints:**
- Use the datetime module to work with dates.
- Use 'open()' in the appropriate mode to read from and write to the file.
- Consider storing task data in a list of dictionaries for easy updating and retrieval.
- Use relative path 'Module3/Lesson5/Exercise1/filename.txt'
"""


