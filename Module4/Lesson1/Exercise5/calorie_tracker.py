calorie_data = {}

def add_food_calories(food, calories):
    calorie_data[food] = calorie_data.get(food, 0) + calories

def get_total_calories():
    return sum(calorie_data.values())