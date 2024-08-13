"""
Exercise 5: City Vehicle Registration System

Instructions:
1. Define a Vehicle Class:
    - Include attributes for registration number, type (car, bike, truck), and owner.
    - Include methods to update the owner and display vehicle details.
2. Implement the DMV System:
    - Create a system to register new vehicles and store them in a collection.
    -Allow updating the owner information for a registered vehicle.
    - Implement a method to display all registered vehicles.
3. User Interaction for Vehicle Registration:
    - Use input functions to register new vehicles, update owner details, and display all vehicles.
    - Use loops and conditional statements to handle different user actions.
4. Data Structures and Error Handling:
    - Use a dictionary to store vehicles, with registration numbers as keys.
    - Apply try-except blocks to handle errors, such as duplicate registrations or invalid inputs.

Explanation:
- The Vehicle class represents individual vehicles, each with a registration number, type, and owner
- The DMV system uses a dictionary to manage vehicle objects. facilitating easy access and modificaiton based on registration numbers
- The user can register new vehicles, update owner information, and view all registered vehicles
- Exception handling ensures the system can handle unexpected situations like duplicate registration numbers or invalid inputs
- This system dmeonstrates the creation and management of multiple objects from a class, each representing a unique entity in the program

Hints:
- Consider using the vehicle;s registration number as a unique identifier
- Ensure the registration number is not duplicated when adding a new vehicle

"""


class Vehicle:
    def __init__(self, reg_num, vehicle_type, owner):
        self.reg_num = reg_num
        self.vehicle_type = vehicle_type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner

    def display_details(self):
        print(f"Registration: {self.reg_num}, Type: {self.vehicle_type}, Owner: {self.owner}")

vehicles = {}

def register_vehicle(reg_num, vehicle_type, owner):
    if reg_num in vehicles:
        print("Error: Registration number already exists.")
        return
    vehicles[reg_num] = Vehicle(reg_num, vehicle_type, owner)
    print(f"Vehicle with registration number {reg_num} registered.")

def update_vehicle_owner(reg_num, new_owner):
    if reg_num in vehicles:
        vehicles[reg_num].update_owner(new_owner) # dict is a key string value of vehicle object
        print(f"Updated owner for vehicle {reg_num}.")
    else:
        print("Vehicle not found.")

def display_all_vehicles():
    for vehicle in vehicles.values():
        vehicle.display_details()


while True:
    action = input("Enter action (register, update, display, exit): ").lower()
    if action == "exit":
        break

    try:
        if action == "register":
            reg_num = input("Enter registration number: ")
            vehicle_type = input("Enter vehicle type: ")
            owner = input("Enter owner name: ")
            register_vehicle(reg_num, vehicle_type, owner)
        elif action == "update":
            reg_num = input("Enter registration number: ")
            new_owner = input("Enter new owner name: ")
            update_vehicle_owner(reg_num, new_owner)
        elif action == "display":
            display_all_vehicles()
    except Exception as e:
        print(f"An error occurred: {e}")

print("DMV System closed.")