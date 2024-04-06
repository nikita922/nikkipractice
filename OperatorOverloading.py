class MyVector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, MyVector):
            # Define the behavior of addition for MyVector
            return MyVector(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Unsupported operand type for +: " + type(other).__name__)

    def __eq__(self, other):
        if isinstance(other, MyVector):
            # Define the behavior of equality for MyVector
            return self.x == other.x and self.y == other.y
        else:
            return False

    def __str__(self):
        return f"({self.x}, {self.y})"

# Create two MyVector instances
v1 = MyVector(1, 2)
v2 = MyVector(3, 4)

# Use the overloaded + and == operators
result = v1 + v2
print(result)  # Output: (4, 6)
print(v1 == v2)  # Output: False
