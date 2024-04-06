number =int(input("Enter a number: "))
num_str = str(number)
num_digits = len(num_str)
total = sum(int(digit) ** num_digits for digit in num_str)

if total == number:
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")