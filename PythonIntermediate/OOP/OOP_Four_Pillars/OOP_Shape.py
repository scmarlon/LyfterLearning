from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius
    
class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length ** 2

    def calculate_perimeter(self):
        return 4 * self.side_length
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)
    


circle1 = Circle(radius=5)
print(f"Area of the circle: {circle1.calculate_area()} and perimeter: {circle1.calculate_perimeter()}")  # Area of the circle: 78.5 and perimeter: 31.4

rectangle1 = Rectangle(length=10, width=5)
print(f"Area of the rectangle: {rectangle1.calculate_area()} and perimeter: {rectangle1.calculate_perimeter()}")  # Area of the rectangle: 50 and perimeter: 30

square1 = Square(side_length=5)
print(f"Area of the square: {square1.calculate_area()} and perimeter: {square1.calculate_perimeter()}")  # Area of the square: 25 and perimeter: 20