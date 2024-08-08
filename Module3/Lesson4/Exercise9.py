
# Exercise 9: Customer Inquiry Response Categorization
"""
Objective:
Create a Python script to categorize customer inquiries from a single text file into different departments using the re.split() function.

Problem Statement:
You are tasked with organizing a large volume of customer inquiries that have been compiled into a single text file. Each inquiry is separated by a special delimiter, "#END#". The inquiries need to be categorized into different departments (Sales, Support, and Billing) based on specific keywords in the text.

Instructions:
1. Read a string representing the compiled customer inquiries.
2. Utilize re.split() to separate individual inquiries using the delimiter.
3. Categorize each inquiry based on keywords: 'purchase' for Sales,
'help' for Support, and 'invoice' for Billing.
4. Implement error handling for categorization and splitting.
5. Display the inquiries categorized under each department.

Hints:
- Create a regex pattern to split the text into separate inquiries using the "#END#" delimiter.
- Analyze each inquiry using regex to identify department-specific keywords.
- Use dictionaries or lists to store inquiries categorized by department.
- Employ try-except blocks to ensure robust processing of each inquiry.

"""

import re

def categorize_inquiry(inquiry):
    if re.search(r"purchase", inquiry, re.IGNORECASE):
        return "Sales"
    elif re.search(r"help", inquiry, re.IGNORECASE):
        return "Support"
    elif re.search(r"invoice", inquiry, re.IGNORECASE):
        return "Billing"
    else:
        return "General"

def process_inquiries(text):
    inquiries = re.split(r"#END#", text)
    categorized_inquiries = {"Sales": [], "Support": [], "Billing": [], "General": []}
    for inquiry in inquiries:
        if inquiry.strip():
            try:
                category = categorize_inquiry(inquiry)
                categorized_inquiries[category].append(inquiry.strip())
            except Exception as e:
                print(f"Error processing inquiry: {e}")
                categorized_inquiries["General"].append(inquiry.strip())
    return categorized_inquiries


# Sample text of customer inquiries
customer_inquiries = """
    I need help with my account. #END#
    How can I purchase a new product? #END#
    Please send my invoice for last month. #END#
    What are your store hours? #END#
"""

# Organizing and displaying categorized inquiries
categorized = process_inquiries(customer_inquiries)
for category, inquiries in categorized.items():
    print(f"{category} Inquiries:")
    for inquiry in inquiries:
        print(f"- {inquiry}")