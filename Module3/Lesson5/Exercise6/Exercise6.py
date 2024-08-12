# Exercise 6: Recipe Collection Manager
"""
Objective: To create a Python program for managing a personal collection of recipes. This exercise will focus on file handling for reading and organizing recipe information, integrating Python concepts like functions, input handling, string manipulation, and try-except blocks, along with data structures such as lists, sets, and dictionaries.

Problem Statement: Your task is to develop a Python program that organizes a collection of recipes stored in a file (recipes_collection.txt). Each line in the file should contain a recipe's name, followed by its ingredients and preparation steps, separated by semicolons (e.g.,
"Chocolate Cake;flour, sugar, cocoa powder;mix, bake"). The program should allow users to add new recipes, search for recipes by ingredient, and list all recipes.

**Instructions:**
1. Read the existing recipes from 'recipes_collection.txt'.
2. Provide a menu with options to Add a New Recipe, Search by Ingredient, and List All Recipes.
3. Implement functionalities for each menu option:
    - **Add a New Recipe:** Prompt for the recipe's name, ingredients, and preparation steps, and add the entry to the file.
    - **Search by Ingredient:** Allow users to enter an ingredient and display all recipes that include it.
    - **List All Recipes:** Display the names of all recipes in the collection.
4. After adding a new recipe, update the 'recipes_collection.txt' file accordingly.
S. Use exception handling for potential file reading and writing errors.
6. Organize the code with functions for each task.

**Hints:**
- Use 'open()' in the appropriate mode to read from and write to the file.
- Consider using 'split()' for parsing lines and string manipulation.
- Store the recipe data in a suitable structure, like a list of dictionaries, for easy manipulation.
- Use relative path 'Module3/Lesson5/Exercise6/recipes_collection.txt'
"""


def read_recipes(filename):
    try:
        with open(filename, 'r') as file:
            recipes = []
            for line in file:
                name, ingredient, steps = line.strip().split(';')
                recipes.append({'name': name, 'ingredients': ingredient.split(','), 'steps': steps})
            return recipes
    except FileNotFoundError:
        []

def write_recipes(filename, recipes):
    with open(filename, 'a') as file:
        last_recipe = recipes[-1]
        file.write(f"{last_recipe['name']};{','.join(last_recipe['ingredients'])};{last_recipe['steps']}\n")

def add_recipe(recipes):
    name = input("Enter recipe name: ")
    ingredients = input("Enter ingredients (comma-separated): ").split(',')
    steps = input("Enter preparation steps: ")
    recipes.append({'name': name, 'ingredients': ingredients, 'steps': steps})

def search_by_ingredient(recipes):
    ingredient = input("Enter ingredient to search for: ")
    found_recipes = [recipe['name'] for recipe in recipes if ingredient in recipe['ingredients']]
    print("Recipes with", ingredient, ":", ','.join(found_recipes))

def list_all_recipes(recipes):
    for recipe in recipes:
        print(recipe['name'])

def main():
    recipes = read_recipes('Module3/Lesson5/Exercise6/recipes_collection.txt')

    while True:
        print("\n1. Add a New Recipe")
        print("2. Search by Ingredient")
        print("3. List All Recipes")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_recipe(recipes)
            write_recipes('Module3/Lesson5/Exercise6/recipes_collection.txt', recipes)
        elif choice == '2':
            search_by_ingredient(recipes)
        elif choice == '3':
            list_all_recipes(recipes)
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main()