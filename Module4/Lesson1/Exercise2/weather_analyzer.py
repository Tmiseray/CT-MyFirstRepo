def read_weather_data(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            day, temp, rain = line.strip().split(', ')
            data.append((int(day), float(temp), float(rain)))
        return data

def calculate_average_temperature(data):
    total_temp = sum(temp for _, temp, _ in data)
    return total_temp / len(data)

def calculate_total_rainfall(data):
    return sum(rain for _, _, rain in data)

def find_highest_temperature_day(data):
    return max(data, key=lambda x: x[1])[0]

