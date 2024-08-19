"""
Exercise 5. Crafting a Weather Forecasting App

Objective:
Develop a Python application to provide weather forecasts, focusing on clean coding principles, including clear naming conventions, modular design, and effective use of Python features like OOP, data structures, and exception handling.

Problem Statement:
You are tasked with creating a weather forecasting app that allows users to check the weather forecast for different cities. 
The app should be user-friendly, efficient, and well-structured, showcasing clean coding practices.

Instructions:
1. Create a class to represent the weather forecasting functionality, including methods for fetching and displaying weather data.
2. Implement user interaction for selecting cities and viewing their weather forecasts.
3. Use dictionaries or lists to manage the data related to cities and their weather.
4. Apply exception handling for user input validatioin and error scenarios
5. Structure your code into different modules to separate the user interface from logic handling the weather data
6. Ensure all variables, functions, and classes have descriptive and meaningful names for clarity.

"""

from weather_forecast import WeatherForecast

def main():
    weather_app = WeatherForecast()
    while True:
        try:
            city = input("Enter a city to get its weather forecast or 'exit' to quit: ")
            if city.lower() == 'exit':
                break
            weather_app.display_weather(city)
        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    main()