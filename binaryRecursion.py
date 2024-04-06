def decimal_to_binary(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_to_binary(n // 2) + str(n % 2)

decimal_number = int(input("Enter the decimal number: "))
binary_equivalent = decimal_to_binary(decimal_number)
print(f"Binary equivalent of {decimal_number} is {binary_equivalent}")
