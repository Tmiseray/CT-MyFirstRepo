
# Exercise 2: Marketing Campaign Email Validator
"""
Objective: 
Python script to validate a list of email addresses for a marketing campaign, ensuring they adhere to a standard email format.

Problem Statement:
You are tasked with preparing an email list for an upcoming marketing campaign. The list contains various email addresses, some of which may not be in the correct format. Your goal is to validate these email addresses, filter out invalid ones, and compile a list of valid email addresses for the campaign.

Instructions:
1. Read a list of email addresses (simulated through a predefined list.
2. Implement a regex pattern to validate the email addresses.
3. Store valid email addresses in one list and invalid ones in another.
4. Handle any errors that might occur during validation.
5. Display both lists of valid and invalid email addresses.

Hints:
- Use re.match() with an appropriate regex pattern to validate each email address. 
- Iterate through the list of emails, applying the validation regex to each.
- Store email addresses in separate lists based on their validity.
- Use try-except blocks to handle exceptions during the validation process.

"""

import re

def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(pattern, email):
        return True
    else:
        return False

def process_emails(email_list):
    valid_emails = []
    invalid_emails = []
    for email in email_list:
        try:
            if validate_email(email):
                valid_emails.append(email)
            else:
                invalid_emails.append(email)
        except Exception as e:
            print(f"Error processing email {email}: {e}")
    return valid_emails, invalid_emails

# Sample list of email addresses
email_list = ["user@example.com", 
              "invalid-email.com", 
              "contact@company.org", 
              "name@domain", 
              "info@example.net"]

# Processing and displaying email addresses
valid, invalid = process_emails(email_list)
print("Valid Emails:", valid)
print("Invalid Emails:", invalid)