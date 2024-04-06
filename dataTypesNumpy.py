import numpy as np

# Specifying data types when creating arrays
arr_int = np.array([1, 2, 3], dtype=np.int32)
arr_float = np.array([1.0, 2.0, 3.0], dtype=np.float64)

# Check the data type of an array
print(arr_int.dtype)
print(arr_float.dtype)

# You can also specify the data type for individual elements
arr_custom = np.array([1, 2, 3], dtype=np.uint16)

print(arr_custom)
