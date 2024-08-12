"""
Exercise 5: Personal Fitness Tracker - Instructions

1. Create Two Custom Modules:
    - Develop a module for calorie tracking (calorie_tracker.py) and another for exercise routines (exercise_tracker.py).
2. Implement Functions in Calorie Tracker Module:
    - In calorie_tracker. py, write functions like:
        - add_food_calories(food, calories): Adds calories for a given food item. 
        - get_total_calories(): Returns the total calories consumed.
3. Implement Functions in Exercise Tracker Module:
    - In exercise_tracker.py, write functions such as:
        - log_exercise(exercise,duration): Logs an exercise with its duration.
        - get_total_exercise_time(): Returns the total time spent on exercises.
4. User Interaction in Main Script:
    - In the main script (main.py), create an interface that allows users to input their daily food intake and exercises.
    - Import and use the functions from both calorie_tracker and exercise_tracker modules.
5. Test the Fitness Tracker:
    - Run the program to ensure that calorie intake and exercise routines are tracked and totaled correctly.

"""
import calorie_tracker as ct
import exercise_tracker as et


def main():
    while True:
        choice = input("Enter '1' to add food, '2' to log exercise, or '3' to show totals: ")
        if choice == '1':
            food = input("Enter food item: ")
            calories = int(input("Enter calories: "))
            ct.add_food_calories(food, calories)
        elif choice == '2':
            exercise = input("Enter exercise: ")
            duration = int(input("Enter duration in minutes: "))
            et.log_exercise(exercise, duration)
        elif choice == '3':
            print(f"Total Calories: {ct.get_total_calories()}")
            print(f"Total Exercise Time: {et.get_total_exercise_time()} minutes")
        else:
            break

if __name__ == '__main__':
    main()