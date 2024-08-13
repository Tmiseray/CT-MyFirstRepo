class Smartphone:
    def __init__(self, model):
        self.model = model

    def make_call(self, number):
        print(f"Making a call to {number}")

    def send_message(self, number, message):
        print(f"Sending message to {number}: {message}")

class SmartCameraPhone(Smartphone): # Inherits from Smartphone
    def __init__(self, model, camera_resolution):
        super().__init__(model) # Call to the superclass constructor
        self.camera_resolution = camera_resolution
        
    def take_photo(self):
        print(f"Taking a photo with {self.camera_resolution} resolution")

    def make_call(self, number):
        # Overriding the make_call method
        print(f"Making a video call to {number} with {self.camera_resolution} resolution")

# Example Usage
basic_phone = Smartphone("PhoneModelBasic")
camera_phone = SmartCameraPhone("PhoneModelPro", "1080p")

# Using the make_call method from the base class
basic_phone.make_call("1234567890") # Output: Making a regular call to 1234567890

# Using the overridden make_call method from the subclass
camera_phone.make_call("0987654321") # Output: Making a video call to 0987654321 with 1080p resolution