"""
Exercise 3: City Traffic Control System

Instructions:
1. Create Vehicle and TrafficSignal Classes:
    - Vehicle class with methods to add a vehicle and display its type.
    - TrafficSignal class with methods to change the signal and display the current signal.
2. Simulate Traffic at an Intersection:
    - Use a loop to simulate time passing, changing traffic signals accordingly.
    - Allow adding vehicles to the intersection and display the current state of the intersection.
3. Implement User Interaction:
    - Use input functions for user actions like adding vehicles and changing signals.
    - Use conditional statements to handle different traffic scenarios based on the signal.
4. Use Modules and Exception Handling:
    - Organize the classes into separate modules for better code management.
    - Apply try-except blocks for handling invalid inputs or operational errors.

Explanation:
- The Vehicle class represents different types of vehicles, with a method to display the vehicle type.
- The TrafficSignal class manages the traffic signals, with methods to change and display the current signal.
- The main program loop allows user interaction for adding vehicles, changing signals, and displaying the current traffic state.
- The use of separate modules (vehicle.py and traffic_signal.py) organizes the code and improves readability.
- Exception handling ensures the system runs smoothly, even when faced with unexpected inputs or errors.

Hints:
- Consider using a list or a set to manage the vehicles at the intersection
- Implement a method to clear the intersection when the signal turns green.
"""