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
- Use relative path 'Module3/Lesson5/Exercise7/daily_tasks.txt'
"""

import datetime

def read_tasks(filename):
    try:
        with open(filename, 'r') as file:
            tasks = []
            for line in file:
                description, due_date, status = line.strip().split(',')
                tasks.append({'description': description, 'due date': due_date, 'status': status})
            return tasks
    except FileNotFoundError:
        return []

def write_tasks(filename, tasks):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(f"{task['description']},{task['due date']},{task['status']}\n")

def add_new_task(tasks, filename):
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    # Validate due_date format and logic here (optional)
    new_task = {'description': description, 'due date': due_date, 'status': 'Pending'}
    tasks.append(new_task)
    with open(filename, 'a') as file:
        file.write(f"{description},{due_date},Pending\n")
    print("Task added successfully.")

def mark_task_completed(tasks):
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task['description']} - Due: {task['due date']} - Status: {task['status']}")
    task_number = int(input("Enter task number to mark as completed: "))
    if 0< task_number <= len(tasks):
        tasks[task_number - 1]['status'] = 'Completed'
    else:
        print("Invalid task number.")

def view_overdue_tasks(tasks):
    today = datetime.date.today().isoformat()
    overdue_tasks = [task for task in tasks if task['due date'] < today and task['status'] == 'Pending']
    for task in overdue_tasks:
        print(f"- {task['description']} - Due: {task['due date']}")

def display_tasks_by_date(tasks):
    specific_date = input("Enter date (YYYY-MM-DD) to view tasks: ")
    tasks_for_date = [task for task in tasks if task['due date'] == specific_date]
    print(f"Tasks for {specific_date}")
    for task in tasks_for_date:
        print(f"- {task['description']} - Status: {task['status']}")

def main():
    tasks = read_tasks('Module3/Lesson5/Exercise7/daily_tasks.txt')

    while True:
        print("\n1. Add a New Task")
        print("2. Mark Task as Completed")
        print("3. View Overdue Tasks")
        print("4. Display Tasks by Date")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_new_task(tasks, 'Module3/Lesson5/Exercise7/daily_tasks.txt')
        elif choice == '2':
            mark_task_completed(tasks)
            write_tasks('Module3/Lesson5/Exercise7/daily_tasks.txt', tasks)
        elif choice == '3':
            view_overdue_tasks(tasks)
        elif choice == '4':
            display_tasks_by_date(tasks)
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main()