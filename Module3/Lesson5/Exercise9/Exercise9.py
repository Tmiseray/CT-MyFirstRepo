# Exercise 9: Unique Travel Destinations Analyzer
"""
Objective: Create a Python program to analyze and report unique travel destinations from a collection of traveler experiences. This exercise will use file handling for processing travel data and incorporate Python concepts such as tuples, sets, functions, string manipulation, and try-except blocks.

Problem Statement: Develop a Python program that helps identify unique travel destinations mentioned in a collection of traveler experiences. The experiences are stored in a file (travel_experiences.txt), with each line containing a traveler's name and a comma-separated list of destinations they've visited (e.g., "John Doe: Paris, London, New York").
The program should extract and list all unique destinations across all travelers.
filename = 'Module3/Lesson5/Exercise9/travel_expenses.txt'

"""


def read_travel_experiences(filename):
    try:
        with open(filename, 'r') as file:
            travel_data = []
            for line in file:
                name, destination = line.strip().split(': ')
                destinations_set = set(destination.split(', '))
                travel_data.append((name, destinations_set))
            return travel_data
    except FileNotFoundError:
        []

def analyze_unique_destinations(travel_data):
    unique_destinations = set()
    for _, destination in travel_data:
        unique_destinations.update(destination)
    return unique_destinations

def main():
    travel_data = read_travel_experiences('Module3/Lesson5/Exercise9/travel_expenses.txt')
    if not travel_data:
        print("No travel data available.")
        return
    
    unique_destinations = analyze_unique_destinations(travel_data)
    print("Unique Travel Destinations:")
    for destination in unique_destinations:
        print(destination)

if __name__ == '__main__':
    main()