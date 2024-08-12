"""
Exercise 4: Currency Exchange Calculator - Instructions

1. Create a Currency Conversion Module:
    - Develop a Python module (currency_converter.py) with functions for different currency conversions, like USD to EUR, GBP to USD, etc.
2. Implement Conversion Functions:
    - In currency_converter. py, define functions such as:
        - usd_to_eur (usd_amount): Converts USD to EUR. 
        - gbp_to_usd (gbp_amount): Converts GBP to USD.
    - Assume fixed exchange rates, for instance, 1 USD = 0.85 EUR, 1 GBP = 1.30 USD.
3. Using Aliasing in Main Script:
    - In the main script (main. py), import the conversion functions with aliases for simplicity and clarity.
    - Example: from currency_converter import usd_to_eur as to_euro, gbp_to_usd as to_usd.
4. User Interaction:
    - Use the input function to ask users for the amount and the currency they want to convert from.
    - Based on the input, use the aliased functions to perform the currency conversion.
5. Test the calculator:
    - Run the program to ensure the currency conversion and aliasing are working correctly.

"""

from currency_converter import usd_to_eur as to_euro, gbp_to_usd as to_usd


def main():
    try:
        amount = float(input("Enter the amount to convert: "))
        currency = input("Enter the currency to convert from (USD or GBP): ").upper()
        if currency == 'USD':
            print(f"{amount} USD is {to_euro(amount)} EUR.")
        if currency == 'GBP':
            print(f"{amount} GBP is {to_usd(amount)} USD.")
        else:
            print("Invalid currency. Please enter 'USD' or 'GBP'.")
    except ValueError:
        print("Please enter a valid numeric amount.")

if __name__ == '__main__':
    main()