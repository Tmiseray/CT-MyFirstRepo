
# Exercise 5: Customer Feedback Analysis for a Restaurant
"""
Objective:
Create a Python script to analyze customer feedback for a restaurant, categorizing comments into feedback about Food service or ambiance using regex.

Problem Statement:
Your restaurant has collected a series of customer feedback comments. The goal is to categorize these comments to better understand customer opinions about different aspects of the restaurant: food, service, and ambiance.

Instructions:
1. Utilize a provided list of customer feedback comments.
2. Develop regex pattern to identify mentions of food, service, and ambiance.
3. Analyze each comment and categorize it into the appropriate feedback category.
4. Implement error handling for any issues in the categorization process.
5. Display the results, showing the number of comments in each category.

Hints:
- Define distinct regex patterns for keywords related to food, service, and ambiance.
- Iterate through the feedback list, applying regex to categorize each comment.
- Use a dictionary to store the count of comments in each category.
- Employ try-except blocks to manage any exceptions during processing.

"""

import re


def categorize_feedback(comment):
    food_pattern = r"\b(taste|delicious|flavor|dish|menu)\b"
    service_pattern = r"\b(service|waiter|staff|host|experience)\b"
    ambiance_pattern = r"\b(ambiance|atmosphere|environment|decor)\b"

    try:
        categories = {"Food": False, "Service": False, "Ambiance": False}
        if re.search(food_pattern, comment, re.IGNORECASE):
            categories["Food"] = True
        if re.search(service_pattern, comment, re.IGNORECASE):
            categories["Service"] = True
        if re.search(ambiance_pattern, comment, re.IGNORECASE):
            categories["Ambiance"] = True
        return categories
    except Exception as e:
        print(f"Error analyzing comment: {e}")
        return categories


feedback_comments = [
    "The ambiance was romantic and cozy.", 
    "Waiters were so friendly and prompt.", 
    "Loved the flavor of the grilled salmon!", 
    "The decor is outdated, but the food tastes great.", 
    "Slow service, but the mabiance made up for it."
]

# Analyzing feedback
feedback_count = {"Food": 0, "Service": 0, "Ambiance": 0}
for comment in feedback_comments:
    feedback = categorize_feedback(comment)
    for category, present in feedback.items():
        if present:
            feedback_count[category] += 1

# Displaying feedback analysis
for category, count in feedback_count.items():
    print(f"{category} Feedback: {count}")
