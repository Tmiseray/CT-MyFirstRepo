
# Exercise 7: Product Code Validation System
"""
Objective:
Create a Python script to validate a list of product codes based on specific formatting rules, using the re.match() function in regex.

Problem Statement:
In a warehouse management system, product codes follow a strict format that combines letters and numbers. Your task is to validate a list of product codes, ensuring they adhere to the format ABC-1234', where 'ABC' represents a series of letters and
'1234' represents a series of numbers.

Instructions:
1. Start with a provided list of product codes.
2. Implement a regex pattern using re.match() to validate each code's format.
3. Categorize and store codes into 'valid' and 'invalid' groups based on the validation.
4. Implement error handling for any anomalies encountered during validation.
5. Display the results, listing both valid and invalid product codes.

Hints:
- Develop a regex pattern that matches the specific format of the product codes.
- Use a loop to process each code in the list, applying the re. match () function for validation.
- Store validated codes in two separate lists: one for valid codes and one for invalid codes.
- Use try-except blocks to ensure robust processing of each code.

"""

