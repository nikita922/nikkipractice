# Create two sets
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# Add an element to a set
set1.add(6)
print("After adding 6 to set1:", set1)

# Remove an element from a set
set2.remove(7)
print("After removing 7 from set2:", set2)

# Union of two sets
union_result = set1.union(set2)
print("Union of set1 and set2:", union_result)

# Intersection of two sets
intersection_result = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection_result)

# Difference of two sets
difference_result = set1.difference(set2)
print("Difference of set1 and set2:", difference_result)

# Symmetric Difference of two sets
symmetric_difference_result = set1.symmetric_difference(set2)
print("Symmetric Difference of set1 and set2:", symmetric_difference_result)
