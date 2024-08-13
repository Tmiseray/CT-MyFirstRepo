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

# Example Usage
basic_phone = Smartphone("PhoneModelBasic")
basic_phone.make_call("1234567890")
basic_phone.send_message("1234567890", "Hello from Basic Phone!")

camera_phone = SmartCameraPhone("PhoneModelPro", "1080p")
camera_phone.make_call("0987654321")
camera_phone.take_photo()