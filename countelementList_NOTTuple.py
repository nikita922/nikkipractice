my_list = [1, 2, 3, 'hello', (4, 5), 6, 7]

# Initialize a counter
count = 0

# Iterate through the list
for item in my_list:
    count += 1
    if isinstance(item, tuple):
        break

# Print the count of elements until a tuple is encountered
print(f"Count of elements until a tuple is encountered: {count}")
