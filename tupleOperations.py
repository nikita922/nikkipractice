# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# Accessing elements
print("Accessing elements:")
print(my_tuple[0])    # Access the first element (1)
print(my_tuple[-1])   # Access the last element (5)

# Slicing
print("\nSlicing:")
sliced_tuple = my_tuple[1:4]  # Creates a new tuple (2, 3, 4)
print(sliced_tuple)

# Concatenating tuples
print("\nConcatenating tuples:")
tuple1 = (1, 2)
tuple2 = (3, 4)
concatenated_tuple = tuple1 + tuple2  # Creates a new tuple (1, 2, 3, 4)
print(concatenated_tuple)

# Tuple repetition
print("\nTuple repetition:")
repeated_tuple = my_tuple * 2  # Creates a new tuple (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
print(repeated_tuple)

# Finding tuple length
print("\nFinding tuple length:")
length = len(my_tuple)  # Returns 5
print(length)

# Iterating through a tuple
print("\nIterating through a tuple:")
for item in my_tuple:
    print(item)

# Checking membership
print("\nChecking membership:")
if 3 in my_tuple:
    print("3 is in the tuple")

# Tuple unpacking
print("\nTuple unpacking:")
a, b, c, d, e = my_tuple
print(f"a: {a}, b: {b}, c: {c}, d: {d}, e: {e}")

# Count and index
print("\nCount and index:")
count = my_tuple.count(3)    # Returns the count of 3 in the tuple
index = my_tuple.index(4)    # Returns the index of the first occurrence of 4
print(f"Count of 3: {count}")
print(f"Index of 4: {index}")
