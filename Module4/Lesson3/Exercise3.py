"""
Exercise 3: Vehicle Rental System

Objective:
Build a vehicle rental system that can manage different types of vehicles, such as cars and bikes. 
The system should be able to handle vehicle rentals, returns, and display available vehicles.

Problem Statement:
A rental service needs a system to manage its fleet of various types of vehicles. 
Each vehicle type has unique attributes and rental rates. 
The system should allow the staff to rent out vehicles, accept returns, and provide an overview of the available fleet.

** Instructions: **
1. Create a base class Vehicle with common attributes like make, model, and rental rate.
2. Develop subclasses Car and Bike that inherit from Vehicle and have additional specific attributes.
3. Implement methods in the classes for renting and returning vehicles, adjusting availability as needed.
4. Create a main program that:
    - Adds new vehicles to the fleet.
    - Handles renting and returning vehicles.
    - Displays available vehicles for rent.
4. Use a list to store the fleet of vehicles and track their availability status.
5. Apply error handling for situations like trying to rent out an already rented vehicle.

Explanation:
This exercise demonstrates the use of inheritance in a vehicle rental system. 
The base class Vehicle contains attributes and methods common to all vehicles. 
The Car and Bike subclasses excend Vehicle by adding specific attributes like car_type and bike_type. 
The system can add new vehicles, rent them out, accept returns, and display available vehicles. 
The use of inheritance simplifies the management of different vehicle types, showcasing how to create a flexible and scalable system.

Hints:
• In the Vehicle class, use a boolean attribute to track whether a vehicle is available or not.
• Override methods in Car and Bike if their rental process differs from the base class.
• In the main program, use a loop with a menu to let the user choose different actions (e.g., rent, return, view available vehicles).

"""

class Vehicle:
    def __init__(self, make, model, rental_rate):
        self.make = make
        self.model = model
        self.rental_rate = rental_rate
        self.is_available = True

    def rent_vehicles(self):
        if self.is_available:
            self.is_available = False
            return True
        return False
    
    def return_vehicles(self):
        self.is_available = True

class Car(Vehicle):
    def __init__(self, make, model, rental_rate, car_type):
        super().__init__(make, model, rental_rate)
        self.car_type = car_type

class Bike(Vehicle):
    def __init__(self, make, model, rental_rate, bike_type):
        super().__init__(make, model, rental_rate)
        self.bike_type = bike_type

def add_vehicle(fleet):
    vehicle_type = input("Enter vehicle type (Car/Bike): ").lower()
    make = input("Enter make: ")
    model = input("Enter model: ")
    rental_rate = float(input("Enter rental rate: "))
    if vehicle_type == 'car':
        car_type = input("Enter car type: ")
        fleet.append(Car(make, model, rental_rate, car_type))
    elif vehicle_type == 'bike':
        bike_type = input("Enter bike type: ")
        fleet.append(Bike(make, model, rental_rate, bike_type))

def rent_vehicle(fleet):
    model = input("Enter model to rent: ")
    for vehicle in fleet:
        if vehicle.model == model and vehicle.rent_vehicles():
            print(f"Rented {model}.")
            return
    print("Vehicle not available.")

def return_vehicle(fleet):
    model = input("Enter the model to return: ")
    for vehicle in fleet:
        if vehicle.model == model:
            vehicle.return_vehicles()
            print(f"Returned {model}.")
            return
    print("Vehicle not found.")

def show_available_vehicles(fleet):
    print("Available Vehicles:")
    for vehicle in fleet:
        if vehicle.is_available:
            print(f"{vehicle.__class__.__name__}: {vehicle.make} {vehicle.model}")


def main():
    fleet = []
    while True:
        print("\n1. Add Vehicle")
        print("2. Rent Vehicle")
        print("3. Return Vehicle")
        print("4. Show Available Vehicles")
        print("5. Exit")
        choice = input("Enter your choice: ")
        try:
            if choice == '1':
                add_vehicle(fleet)
            elif choice == '2':
                rent_vehicle(fleet)
            elif choice == '3':
                return_vehicle(fleet)
            elif choice == '4':
                show_available_vehicles(fleet)
            elif choice == '5':
                break
            else:
                print("Invalid choice.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
