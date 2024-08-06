
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

