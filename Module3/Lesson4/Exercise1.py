
# Exercise 1: E-Commerce Product Data Extraction

"""
Objective:
To develop a Python script that efficiently extracts and organizes product information from a text data source, replicating a common task in e-commerce data management.

Problem Statement:
In an e-commerce setting, you are faced with a large text file containing detailed product information. The challenge is to parse this semi-structured data to extract relevant details such as product IDs, names, categories, and prices, and then store this information for easy access and analysis.

Instructions:
1. Read a string that contains product information (simulating data from a file).
2. Implement a regex pattern to identify and extract the necessary product details.
3. Store and organize the extracted data into a structured format, like a list of dictionaries.
4. Incorporate error handling for potential data parsing issues.
5. Display the organized data in a readable format for end-users.

Hints:
- Utilize re.findall() for pattern-based data extraction.
- Craft a regex pattern tailored to the specific data format of the product details.
- Use dictionaries for storing individual product data, and a list to hold all products.
- Implement loops to process and store each extracted product.
- Apply try-except blocks to gracefully handle any parsing errors.

"""

import re


def extract_product_info(data):
    
    product_pattern = r"Product ID: (\d+), Name: (.*?), Category: (.*?), Price: \$(\d+\.\d+)"

    try:
        products = re.findall(product_pattern, data)
        product_list = []
        for product in products:
            product_dict = {
                "ID": product[0],
                "Name": product[1],
                "Category": product[2],
                "Price": product[3]
            }
            product_list.append(product_dict)
        return product_list
    except Exception as e:
        print("An error occurred:", e)
        return []


data = """
        Product ID: 1001, Name: Alpha Widget, Category: Widgets, Price: $19.99
        Product ID: 1002, Name: Beta Widget, Category: Widgets, Price: $29.99
        Product ID: 1003, Name: Gamma Widget, Category: Gadgets, Price: $9.99
        """

# Extracting and displaying product information
product_info = extract_product_info(data)
for product in product_info:
    print(f"Product ID: {product['ID']}, Name: {product['Name']}, Category: {product['Category']}, Price: ${product['Price']}")