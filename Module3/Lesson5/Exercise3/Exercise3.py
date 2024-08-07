# Exercise 3: Weather Data Analysis
"""
Objective: To create a Python program that analyzes historical weather data. This exercise will involve processing and interpreting data from a weather log file, integrating Python concepts such as file handling, string manipulation, functions, conditional and loop statements, and using data structures like lists and dictionaries.

Problem Statement: You are tasked to develop a Python program that processes weather data stored in a file (weather_data.txt). Each line in the file contains a date, temperature (in Celsius), and rainfall (in mm), separated by commas (e.g., "2023-03-15, 16,5"). The program should analyze this data to provide insights such as the average temperature, days with rainfall above a certain threshold, and temperature trends.

**Instructions:**
1. Read the weather data from 'weather_data.txt'.
2. Implement a menu with options to calculate average temperature, list days with significant rainfall, and analyze temperature trends.
3. Implement functionalities for each menu option:
    - **Calculate Average Temperature:** Compute and display the average temperature.
    - **List Days with Significant Rainfall:** Input a rainfall threshold and list all days with rainfall exceeding this threshold.
    - **Analvze Temperature Trends:** Show days with a temperature increase or decrease compared to the previous day.
4. Use exception handling for potential file reading errors.
5. Organize the code with functions for each analysis task.

**Hints:**
- Use 'open()' for reading the file and 'split()' to parse each line.
- Store the data in a suitable structure, like a list of dictionaries, for easy manipulation.
- Utilize list comprehensions and aggregation functions for concise data processing.
- Use relative path 'Module3/Lesson5/Exercise1/filename.txt'
"""


