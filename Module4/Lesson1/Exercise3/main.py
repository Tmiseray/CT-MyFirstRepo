"""
Exercise 3: Recipe Ingredient Converter - Instructions

1. Create a Conversion Module:
    - Create a Python module (unit_converter. py) with functions for different unit conversions, such as cups to milliliters, teaspoons to milliliters, etc.
2. Implement Conversion Functions:
    - In unit_converter.py, write specific functions like:
        - cups_to_milliliters(cups): Converts cups to milliliters. 
        - teaspoons_to_milliliters(teaspoons): Converts teaspoons to milliliters.
    - Assume 1 cup = 237 milliliters and 1 teaspoon = 4.93 milliliters.
3. User Interaction in Main Script:
    - In the main script (main. py), use the input function to ask the user for the ingredient quantity and the unit they want to convert from.
    - Import and use the specific functions from the unit_converter module based on the user's choice.
4. Error Handling:
    - Include try-except blocks in main. py to handle invalid inputs like non-numeric values.
5. Test the Converter:
    - Run the program to test various conversions, ensuring each function in the module works as expected.

"""

from unit_converter import cups_to_milliliters, teaspoons_to_milliliters

def main():
    try:
        quantity = float(input("Enter the quantity of the ingredient: "))
        unit = input("Enter the unit to convert from (cups or teaspoons): ")
        if unit == 'cups':
            print(f"{quantity} cups is {cups_to_milliliters(quantity)} milliliters.")
        elif unit == 'teaspoons':
            print(f"{quantity} teaspoons is {teaspoons_to_milliliters(quantity)} milliliters.")
        else:
            print("Invalid unit. Please enter 'cups' or 'teaspoons'.")
    except ValueError:
        print("Please enter a valid numeric quantity.")

if __name__ == '__main__':
    main()
