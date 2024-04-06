class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14159 * self.radius

# Usage
radius = float(input("Enter the radius of the circle: "))
circle = Circle(radius)
print("Area:", circle.area())
print("Perimeter:", circle.perimeter())
