
# Exercise 8: Conference Badge Registration System
"""
Objective:
Develop a Python script to validate attendee registration details for a conference, focusing on the correctness of badge IDs using the re.match() function.

Problem Statement:
You are helping to manage a professional conference. Each attendee has a badge ID, which follows a specific format: two uppercase letters, a dash, and three digits (e.g., 'AB-123'). Your task is to validate a list of badge IDs, ensuring they comply with this format.

Instructions:
1. Start with a list of badge IDs provided by attendees.
2. Create a regex pattern using re.match() to validate the format of each badge ID.
3. Separate the badge IDs into 'valid' and 'invalid' categories based on their format.
4. Implement error handling for any issues encountered during the validation process.
5. Display the categorized badge IDs, showing which are valid and which are invalid.

Hints:
• Construct a regex pattern that matches the specific badge ID format.
• Iterate through the list of badge IDs, using re.match() to validate each ID.
• Use two separate lists to store and differentiate valid and invalid badge IDs.
• Apply try-except blocks for robust processing and error handling.

"""

import re


def validate_badge_id(badge_id):
    pattern = r"^[A-Z]{2}-\d{3}$"
    if re.match(pattern, badge_id):
        return True
    return False

def process_badge_ids(ids):
    valid_ids = []
    invalid_ids = []
    for id in ids:
        try:
            if validate_badge_id(id):
                valid_ids.append(id)
            else:
                invalid_ids.append(id)
        except Exception as e:
            print(f"Error processing badge ID {id}: {e}")
            invalid_ids.append(id)
    return valid_ids, invalid_ids

badge_ids = ["AB-123", "XY-456", "A-789", "CD-12", "EF-345"]

# Validating and categorizing badge IDs
valid, invalid = process_badge_ids(badge_ids)
print("Valid Badge IDs:", valid)
print("Invalid Badge IDs:", invalid)

