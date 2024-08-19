class WeatherForecast:
    def __init__(self):
        self.city_weather = {'New York': 'Sunny', 'London': 'Rainy', 'Tokyo': 'Cloudy'}

    def get_weather(self, city):
        return self.city_weather.get(city, "Weather data not available")
    
    def display_weather(self, city):
        forecast = self.get_weather(city)
        print(f"Weather in {city}: {forecast}")