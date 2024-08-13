"""
Exercise 5: Shape Area Calculator

Objective:
Create a program to calculate the area of different geometric shapes, demonstrating polymorphism in Python.

Problem Statement:
A graphic design software needs a feature to calculate the area of various shapes like circles, rectangles, and triangles.
While each shape calculates its area differently, the software should handle them through a uniform interface.

** Instructions: **
1. Define a base class Shape with a method calculate_area (without implementation).
2. Create subclasses Circle, Rectangle, and Triangle, each overriding the calculate_area method.
3. Implement a function in the main program to accept a Shape object and call its calculate_area method.
4. Use polymorphism to allow the same function to calculate the area for any shape.
5. Handle invalid shape dimensions or operations using try-except blocks.

Explanation:
This exercise demonstrates polymorphism through a shape area calculator. 
The Shape class provides a interface with the calculate_area method. 
Each subclass (Circle, Rectangle, Triangle) overrides this method to calculate its specific area. 
The get_area function, using polymorphism, can calculate the area of anv shade obiect passed to it, regardless of the shape's specific type. 
This setup allows for easy extension to include more shapes in the future without modifying the existing code structure, showcasing the flexibility and scalability benefits of polymorphism in object-oriented design.

Hints:
• In subclasses, use appropriate formulas to calculate the area of each shape.
• Utilize the isinstance function to ensure that the object passed to the area calculation function is a subclass of Shape.
• Consider using Python's math module for mathematical operations, especially for the circle's area calculation.

"""
import math

class Shape:
    def calculate_area(self):
        raise NotImplementedError("Calculate area method not implemented.")
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height
    
def get_area(shape):
    if isinstance(shape, Shape):
        return shape.calculate_area()
    else:
        raise TypeError("Invalid shape type.")
    
def main():
    circle = Circle(5)
    rectangle = Rectangle(10, 5)
    triangle = Triangle(10, 8)

    shapes = [circle, rectangle, triangle]
    for shape in shapes:
        try:
            area = get_area(shape)
            print(f"The area of the {shape.__class__.__name__} is {area}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()