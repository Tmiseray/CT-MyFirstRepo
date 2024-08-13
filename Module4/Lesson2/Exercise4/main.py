"""
Exercise 4: City Event Planner System

Instructions:
1. Create Event Class and EventManager Module:
    - The Event class should have methods to add an event, register participants, and display event details.
    - Organize the Event class in an EventManager module.
2. Implement File Handling for Event Details:
    - Use text file handling to save and read event details.
    - Ensure the system can store event information in a file and retrieve it when needed.
3. User Interaction for Event Management:
    - Use input functions to add events, register participants, and display event details.
    - Implement loops and conditional statements for handling various actions.
4. Exception Handling and Data Structures:
    - Use try-except blocks for managing file handling errors and invalid inputs.
    - Utilize lists, dictionaries, or tuples to manage events and participants.

Explanation:
- The Event class in the event_manager module handles individual event details and participant registration
- The main program manages a collection of events, allowing the user to add events, register participants, and save or display event details
- File handling is user to store event details in a file (events.txt) and load them when the program starts
- Excepetion handling ensures the system is robust, especially in file operations and user inputs
- Data structures like dictionaries (for managing events) and lists (for paticipants) efficiently organize the data.

Hints:
- Consider using a dictionary to manage events with their names as keys
- Implement a function to format event details neatly before saving them to a file

"""
from event_manager import Event
import os

events = {} # dictionary where the key is the name and the value is the event object

def save_events_to_file():
    with open('Module4/Lesson2/Exercise4/events.txt', 'w') as file:
        for event in events.values():
            file.write(f"{event.name},{event.date},{event.location},{','.join(event.participants)}\n")

def load_events_from_file():
    if os.path.exists('Module4/Lesson2/Exercise4/events.txt'):
        with open('Module4/Lesson2/Exercise4/events.txt', 'r') as file:
            for line in file:
                name, date, location, *participants = line.strip().split(',')
                event = Event(name, date, location)
                event.participants = participants
                events[name] = event


load_events_from_file()

while True:
    action = input("Enter action (add, register, display, save, exit): ").lower()
    if action == "exit":
        break

    try:
        if action == "add":
            name = input("Enter event name: ")
            date = input("Enter event date: ")
            location = input("Enter event location: ")
            events[name] = Event(name, date, location)
        elif action == "register":
            event_name = input("Enter event name: ")
            participant = input("Enter participant name: ")
            if event_name in events:
                events[event_name].register_participant(participant)
            else:
                print("Event not found.")
        elif action == "display":
            for event in events.values():
                event.display_event()
        elif action == "save":
            save_events_to_file()
            print("Events saved to file.")
    except Exception as e:
        print(f"An error occurred: {e}")

print("Event Planner System closed.")
