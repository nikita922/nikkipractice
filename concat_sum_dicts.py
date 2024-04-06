# Define two dictionaries
dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 5, 'c': 15, 'd': 25}

# Concatenate the two dictionaries
concatenated_dict = {**dict1, **dict2}

# Calculate the sum of all values in the concatenated dictionary
total_sum = sum(concatenated_dict.values())

# Display the concatenated dictionary and the sum
print("Concatenated Dictionary:")
print(concatenated_dict)
print(f"Sum of all values: {total_sum}")
