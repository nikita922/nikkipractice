class MathOperations:
    def add(self, *args):
        return sum(args)

math_obj = MathOperations()
result1 = math_obj.add(2, 3)
result2 = math_obj.add(2, 3, 4)
print("Result with 2 arguments:", result1)
print("Result with 3 arguments:", result2)
