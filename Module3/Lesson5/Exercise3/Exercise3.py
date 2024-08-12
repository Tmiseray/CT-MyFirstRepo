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
- Use relative path 'Module3/Lesson5/Exercise3/weather_data.txt'
"""

def read_weather_data(filename):
    try:
        with open(filename, 'r') as file:
            weather_data = []
            for line in file:
                date, temp, rainfall = line.strip().split(',')
                weather_data.append({'date': date, 'temperature': float(temp), 'rainfall': float(rainfall)})
            return weather_data
    except FileNotFoundError:
        return []

def calculate_average_temperature(weather_data):
    total_temp = sum(item['temperature'] for item in weather_data)
    avg_temp = total_temp / len(weather_data)
    print(f"Average Temperature: {avg_temp:.2f}F")

def list_significant_rainfall(weather_data, threshold):
    significant_days = [item['date'] for item in weather_data if item['rainfall'] > threshold]
    print("Days with significant rainfall:")
    for day in significant_days:
        print(day)

def analyze_temperature_trends(weather_data):
    print("Temperature Trends:")
    for i in range(1, len(weather_data)):
        temp_diff = weather_data[i]['temperature'] - weather_data[i - 1]['temperature']
        trend = 'increased' if temp_diff > 0 else 'decreased'
        print(f"{weather_data[i]['date']}: Temperature {trend} by {abs(temp_diff):.2f}F")


def main():
    weather_data = read_weather_data('Module3/Lesson5/Exercise3/weather_data.txt')
    if not weather_data:
        print('No weather data available.')
        return
    
    while True:
        print("\n1. Calculate Average Temperature")
        print("2. List Days with Significant Rainfall")
        print("3. Analyze Temperature Trends")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            calculate_average_temperature(weather_data)
        elif choice == '2':
            threshold = float(input("Enter rainfall thresholld (mm): "))
            list_significant_rainfall(weather_data, threshold)
        elif choice == '3':
            analyze_temperature_trends(weather_data)
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()