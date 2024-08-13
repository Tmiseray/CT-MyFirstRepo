"""
Exercise 4: Smart Home Automation System

Objective:
Develop a smart home automation system that can control various smart devices.
Each device type should have unique functionalities, but all share some common controls.

Problem Statement:
In a modern smart home, various devices like lights, thermostats, and security cameras need to be managed through a centralized system. 
While each device has specific functions, they all share some common controls such as turning on/off and restting.

** Instructions: **
1. Create a base class SmartDevice with common methods like turn_on, turn_off, and reset.
2. Develop subclasses for specific devices: SmartLight, SmartThermostat, and SmartCamera. Each subclass should override some of the base class methods to implement device-specific behavior.
3. Implement a main program that allows users to interact with and control different smart devices.
4. Use method overriding to customize the behavior of common methods for each specific device.
5. Handle any user input errors or invalid operations using try-except blocks.

Explanation:
In this exercise, the SmartDevice class represents a generic smart device with. basic functionalities. 
The subclasses SmartLight, SmartThermostat, and SmartCamera eacn override some of these methods to provide specific behaviors, demonstrating method overriding. 
For example, the turn_on method behaves differently for a light, a thermostat, and a camera, reflecting their unique functions in a smart home system. 
This exercise showcases how method overriding can be used to implement polymorphic behavior in an object-oriented system, allowing for more flexible and intuitive interactions with different types of objects.

Hints:
• In the SmartDevice class, use print statements to simulate turning on/off and resetting the device.
• Override these methods in the subclasses to reflect the specific actions of each device.
• Use a list or dictionary to store and manage multiple devices in the main program.

"""

class SmartDevice:
    def turn_on(self):
        print("Smart Device is turning on.")

    def turn_off(self):
        print("Smart Device is turning off.")

    def reset(self):
        print("Smart Device is resetting.")

class SmartLight(SmartDevice):
    def turn_on(self):
        print("Smart Light is brightening.")

    def turn_off(self):
        print("Smart Light is dimming.")

class SmartThermostat(SmartDevice):
    def turn_on(self):
        print("Smart Thermostat is heating.")

    def turn_off(self):
        print("Smart Thermostat is cooling.")

class SmartCamera(SmartDevice):
    def reset(self):
        print("Smart Camera is recalibrating focus and angle.")

def manage_device(device):
    action = input("Enter action (turn on/turn off/reset): ")
    if action == 'turn on':
        device.turn_on()
    elif action == 'turn off':
        device.turn_off()
    elif action == 'reset':
        device.reset()
    else:
        print("Invalid action.")

def main():
    devices = {
        "light": SmartLight(),
        "thermostat": SmartThermostat(),
        "camera": SmartCamera()
    }
    while True:
        device_name = input("Enter device (light/thermostat/camera/exit): ").lower()
        if device_name == 'exit':
            break
        if device_name in devices:
            manage_device(devices[device_name])
        else:
            print("Device not found.")

if __name__ == '__main__':
    main()