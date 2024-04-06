my_dict = {}
my_dict['name'] = 'Hello'
my_dict['age'] = 31
my_dict['city'] = 'Chembur'
print("Dictionary after adding key-value pairs:")
print(my_dict)
search_key = 'age'
if search_key in my_dict:
    print(f"The value for key '{search_key}' is: {my_dict[search_key]}")
else:
    print(f"Key '{search_key}' not found in the dictionary")
delete_key = 'city'
if delete_key in my_dict:
    del my_dict[delete_key]
    print(f"Key '{delete_key}' deleted from the dictionary")
else:
    print(f"Key '{delete_key}' not found in the dictionary")

print("Dictionary after deleting a key:")
print(my_dict)
