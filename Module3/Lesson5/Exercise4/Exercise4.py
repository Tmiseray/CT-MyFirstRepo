# Exercise 4: Customer Feedback Analysis System
"""
Objective: Develop a Python program to analyze and categorize customer feedback from a file. This exercise involves file handling for reading customer comments, integrating Python concepts like string manipulation, functions, conditional statements, loops, and data structures such as lists and dictionaries for categorizing feedback.

Problem Statement: You need to create a Python program to process customer feedback stored in a file (customer_feedback.txt). Each line in the file contains a customer's name and their comment, separated by a colon (e.g., "John Doe: Loved the product, excellent quality!"). The program should categorize these comments into positive, negative, and neutral feedback based on certain keywords and provide a summary.

**Instructions:**
1. Read customer feedback from 'customer_feedback.txt'
2. Categorize each comment as positive, negative, or neutral based on keywords (e.g., 'good', 'excellent', for positive; 'bad', 'poor' for negative).
3. Implement a menu with options to display categorized feedback and overall summary.
4. For the summary, count and display the of comments in each category.
5. Use exception handling for potential file reading errors.
6. Organize the code using functions for reading data, categorizing comments, and displaying results.

**Hints:**
- Use 'open()' to read the file and 'split()' to separate customer names from their comments.
- Consider creating a dictionary to store categorized comments.
- Use lists to define keywords for categorizing comments.
- Use relative path 'Module3/Lesson5/Exercise4/customer_feedback.txt'
"""

def read_feedback(filename):
    try:
        with open(filename, 'r') as file:
            feedback = []
            for line in file:
                name, comment = line.strip().split(': ')
                feedback.append({'name': name, 'comment': comment})
            return feedback
    except FileNotFoundError:
        []

def categorize_comments(feedback):
    positive_keywords = ['good', 'excellent', 'happy', 'satisfied']
    negative_keywords = ['bad', 'poor', 'unhappy', 'disappointed']
    categorized = {'positive': [], 'negative': [], 'neutral': []}

    for item in feedback:
        comment = item['comment'].lower()
        if any(word in comment for word in positive_keywords):
            categorized['positive'].append(item)
        elif any(word in comment for word in negative_keywords):
            categorized['negative'].append(item)
        else:
            categorized['neutral'].append(item)
    return categorized

def display_categorized_feedback(categorized):
    for category, comments in categorized.items():
        print(f"\n{category.capitalize()} Feedback:")
        for item in comments:
            print(f"- {item['name']}: {item['comment']}")

def display_summary(categorized):
    print("\nFeedback Summary:")
    for category, comments in categorized.items():
        print(f"{category.capitalize()}: {len(comments)} comments")

def main():
    feedback = read_feedback('Module3/Lesson5/Exercise4/customer_feedback.txt')
    if not feedback:
        print("No feedback available.")
        return
    
    categorized = categorize_comments(feedback)

    while True:
        print("\n1. Display Categorized Feedback")
        print("2. Display Summary")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_categorized_feedback(categorized)
        elif choice == '2':
            display_summary(categorized)
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main()
