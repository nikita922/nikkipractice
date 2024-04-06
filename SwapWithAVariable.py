# Swap without using the third variable
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
print("Numbers Before swapping a: {} and b: {}".format(a,b) )
a = a + b
b = a - b
a = a - b
print("Numbers after swapping a: {} and b: {}".format(a,b) )