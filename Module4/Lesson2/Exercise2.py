"""
Exercise 2: Apartment Management System

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

class ApartmentBuilding:
    shared_facilities = ['Gym', 'Swimming Pool', 'Parking Lot']

    def __init__(self, name, total_units):
        self.name = name
        self.total_units = total_units
        self.occupied_units = 0

    def update_occupancy(self, change):
        if 0 <= self.occupied_units + change <= self.total_units:
            self.occupied_units += change
            return True
        return False
    
    def available_units(self):
        return self.total_units + self.occupied_units
    
    def occupancy_rate(self):
        return (self.occupied_units / self.total_units) * 100



buildings = [] # List of ApartmentBuilding Objects

while True:
    action = input("Enter action (add, update, list, exit): ").lower()
    if action == "exit":
        break

    try:
        if action == "add":
            name = input("Enter building name: ")
            units = int(input("Enter total units: "))
            buildings.append(ApartmentBuilding(name, units))
            print(f"Building '{name}' added with {units} units.")
        elif action == "update":
            name = input("Enter building name to update occupancy: ")
            change = int(input("Enter change in occupied units: "))
            for building in buildings:
                if building.name == name:
                    if building.update_occupancy(change):
                        print(f"Updated occupancy for '{name}'.")
                    else:
                        print("Invalid occupancy change.")
                    break
            else:
                print("Building not found.")
        elif action == "list":
            for building in buildings:
                print(f"{building.name}: {building.available_units()} available units, "
                      f"Occupancy rate: {building.occupancy_rate():.2f}%")
    except ValueError:
        print("Invalid input, please enter numeric values for units.")
    except Exception as e:
        print(f"An error occurred: {e}")

print("Apartment management system closed.")