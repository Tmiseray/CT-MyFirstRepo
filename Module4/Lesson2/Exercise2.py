"""
Exercise 2: City Library Management System

Instructions:
1. Define an ApartmentBuilding Class:
    - Include class variables for facilities across all buildings.
    - Use instance variables to track each building's name, total units, and occupied units.
2. Building Management Methods:
    - Implement methods to add new buildings, update occupancy, and list facilities.
    - Include functionality to check for available units in a building.
3. User Interaction:
    - Use input functions to allow the user to interact with the system.
    - Implement loops and conditional statements for different user actions
4. Data Structures and Error Handling:
    - Use a list to manage a collection of ApartmentBuilding objects.
    - Apply exception handling to manage errors, such as trying to occupy an already full building.

Explanation:
- The ApartmentBuilding class represents each apartment building, with shared facilites as a class variable and individual attributes.
- The update_occupancy method allows updating the number of occupied units, within valid limits.
- The available_units and occupancy_rate methods provide information about each building.
- The main program loop lets the user add new buildings, update occupancy. and list all buildings with their details.
- Exception handling ensures input errors are managed effectively.

Hints:
- Remember to update the occupancy status when a new unit is filled or vacated.
- Consider implementing a method to calculate the percentage of occupied units in each building.

"""