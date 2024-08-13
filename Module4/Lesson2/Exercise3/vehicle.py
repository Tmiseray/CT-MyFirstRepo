class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

    def display_type(self):
        print(f"Vehicle Type: {self.vehicle_type}")