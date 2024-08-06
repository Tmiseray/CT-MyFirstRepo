
# Exercise 6: Library Book Sorting System
"""
Objective:
Develop a Python script to sort a list of library book titles into different genres based on specific keywords in their titles using regex.

Problem Statement:
You're assisting a library in organizing their books more efficiently. The library has a list of book titles, each belonging to different genres like Fiction, Non-Fiction, Science, and History. Your task is to categorize these books into their respective genres based on keywords in their titles.

Instructions:
1. Work with a predefined list of book titles.
2. Create regex patterns to identify keywords associated with each genre.
3. Sort each book into the appropriate genre category based on its
title.
4. Handle any exceptions or ambiguous cases in categorization.
5. Display the sorted list of books, categorized by genre.

Hints:
• Define distinct regex patterns for each genre based on title keywords.
• Use a loop to process each book title, applying regex to determine its genre.
• Store the sorted books in a dictionary with genres as keys and lists of titles as values.
• Implement try-except blocks to handle titles that don't clearly fit into any category.

"""

import re


def sort_books(title):
    genre_patterns = {
        "Fiction": r"\b(Adventure|Novel|Story)\b", 
        "Non-Fiction": r"\b(Biography|Memoir|Essay)\b", 
        "Science": r"\b(Physics|Chemistry|Biology)\b", 
        "History": r"\b(Historic|Ancient|Medieval)\b", 
    }
    for genre, pattern in genre_patterns.items():
        if re.search(pattern, title, re.IGNORECASE):
            return genre
    return "General"

def organize_books(titles):
    sorted_books = {"Fiction": [], "Non-Fiction": [], "Science": [], "History": [], "General": []}
    for title in titles:
        try:
            genre = sort_books(title)
            sorted_books[genre].append(title)
        except Exception as e:
            print(f"Error sorting book {title}: {e}")
            sorted_books["General"].append(title)
    return sorted_books


# Sample list of book titles
book_titles = [
    "The Adventure of Sherlock Holmes", 
    "Einstein: His Life and Universe", 
    "The Art of War: Ancient Strategies", 
    "Introduction to Quantum Physics", 
    "The Story of Human Language"
]

# Organizing and displaying sorted books
books_by_genre = organize_books(book_titles)
for genre, books in books_by_genre.items():
    print(f"{genre} Books: {books}")
