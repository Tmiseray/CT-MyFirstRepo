
# Exercise 3: Retail Inventory Categorization
"""
Objective:
Create a Python script to categorize products in a retail inventory based on their codes, using regex to identify different product categories.

Problem Statement:
You are managing a retail inventory system that includes a diverse range of products, each identified by a unique code. These codes follow a specific pattern, indicating the product category. Your task is to categorize these products into different groups based on their codes for better inventory management.

Instructions:
1. Work with a provided list of product codes.
2. Develop regex patterns to identify different product categories (e.g., Electronics, Clothing, Groceries).
3. Categorize each product into the appropriate group based on its code.
4. Handle any exceptions or errors in categorization.
5. Display the categorized list of products, grouped by their categories.

Hints:
- Define specific regex patterns for each category based on the code structure.
- Iterate through the list of product codes, using regex to determine each product's category.
- Use a dictionary to store categorized products, with category names as keys and lists of product codes as values.
- Implement try-except blocks for robust error handling during the categorizing process.

"""

import re

def categorize_product(code):
    categories = {
        "Electronics": r"EL\d{4}", 
        "Clothing": r"CL\d{4}", 
        "Groceries": r"GR\d{4}", 
    }
    for category, pattern in categories.items():
        if re.match(pattern, code):
            return category
    return "Unknown"

def organize_inventory(codes):
    categorized_inventory = {"Electronics": [], "Clothing": [], "Groceries": [], "Unknown": []}
    for code in codes:
        try:
            category = categorize_product(code)
            categorized_inventory[category].append(code)
        except Exception as e:
            print(f"Error processing code {code}: {e}")
            categorized_inventory["Unknown"].append(code)
    return categorized_inventory

product_codes = ["EL1001", "CL2002", "GR3003", "EL1004", "XX9999"]

# Organizing and displaying categorized inventory
inventory = organize_inventory(product_codes)
for category, items in inventory.items():
    print(f"{category}: {items}")
