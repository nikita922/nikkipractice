input_string = "Hello This is Python 123"
upper_count=0
lower_count=0
digit_count=0
for char in input_string:
    if char.isupper():
        upper_count+=1

for char in input_string:
    if char.islower():
        lower_count+=1

for char in input_string:
    if char.isdigit():
        digit_count+=1

print("Uppercase letters:", upper_count)
print("Lowercase letters:", lower_count)
print("Digits:", digit_count)
