from functools import reduce
numbers = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100]
filtered_list = list(filter(lambda x: x % 2 == 0, numbers))
mapped_list = list(map(lambda x: x ** 2, numbers))
reduced_value = reduce(lambda x, y: x + y, numbers)
print("Filtered List:", filtered_list)
print("Mapped List:", mapped_list)
print("Reduced Value:", reduced_value)
