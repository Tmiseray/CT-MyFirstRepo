# Exercise 5: Event Attendance Tracker
"""
Objective: Develop a Python program to track and manage attendance for various events.
The program will involve file handling for storing and retrieving attendance data and integrate Python concepts such as functions, input handling, string manipulation, and try-except blocks, along with data structures like lists and dictionaries.

Problem Statement: You are tasked with creating a Python program to manage attendance records for a series of local events. The attendance data will be stored in a file (event_attendance.txt), with each line containing an event's name, date, and a comma-separated list of attendee names (e.g., "Python Workshop,2023-03-21,John Doe, Jane Smith"). The program should allow for adding new events, registering attendees, and generating attendance reports.

**Instructions:**
1. Read the existing attendance data from event _attendance. txt* .
2. Provide a menu with options to Add a New Event, Register an Attendee, and Generate Attendance Report.
3. Implement functionalities for each menu option:
    - **Add a New Event:** Prompt for the event's name and date, and create an entry.
    - **Register an Attendee:** Allow adding an attendee's name to an existing event.
    - **Generate Attendance Report:** Display a last of events with their respective attendees.
4. After each operation, update the 'event_attendance.txt' file accordingly.
5. Use exception handling for potential file reading and writing errors.
6. Organize the code with functions for each functionality.

**Hints: **
- Use 'open()' in the appropriate mode to read from and write to the file.
- Consider using 'split()' for parsing lines and 'join()' for reconstructing them.
- Store the event data in a dictionary with event names as keys and lists of attendees as values.
- Use relative path 'Module3/Lesson5/Exercise1/filename.txt'
"""

