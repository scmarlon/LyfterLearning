class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        area = 3.14 * self.radius ** 2
        return area

circle1 = Circle(5)
circle2 = Circle(10)
circle3 = Circle(15)
for circle in [circle1, circle2, circle3]:
    print(f"Circle with radius {circle.radius} has area: {circle.get_area()}")