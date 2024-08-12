"""
Exercise 2: Weather Data Analyzer - Instructions

1. Create a Custom Module:
    - Create a Python module (weather_analyzer. py) that contains functions to process weather data.
2. Design Functions In the Module.
    - Implement functions in your module:
        - read_weather_data(filename): Reads weather data from a file and returns it as a list of tuples. 
        - calculate_average_temperature(data): Calculates and returns the average temperature.
        - calculate_total_rainfall(data): Calculates and returns the total rainfall.
        - find_highest_temperature_day (data): Finds and returns the day with the highest temperature.
3. Data Format in Text Files:
    - Assume each line in the text files follows this format: Day, Temperature, Rainfall 
    - Example of a line in a file: 1, 23.5, 5
4. User Interface:
    - In your main Python file (main. py), create an interface that allows the user to input the filename and then displays the calculated weather statistics.
5. Error Handling:
    - Include try-except blocks to handle potential errors, such as file not found or incorrect data format.
6. Test Your Analyzer:
    - Create a few sample text files with weather data and use them to test your weather data analyzer.

"""

import weather_analyzer

def main():
    filename = input("Enter the weather data file name: ")
    try:
        data = weather_analyzer.read_weather_data(filename)
        avg_temp = weather_analyzer.calculate_average_temperature(data)
        total_rainfall = weather_analyzer.calculate_total_rainfall(data)
        highest_temp_day = weather_analyzer.find_highest_temperature_day(data)

        print(f"Average Temperature: {avg_temp:.2f}C")
        print(f"Total Rainfall: {total_rainfall}mm")
        print(f"Highest Temperature on Day: {highest_temp_day}")
    except FileNotFoundError:
        print("File not found. Please check the file name.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()