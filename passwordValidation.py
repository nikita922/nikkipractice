# Password validation criteria
import re

# Maximum number of password attempts
max_attempts = 3

while max_attempts > 0:
    password = input("Enter your password: ")
    if 6 <= len(password) <= 16 and re.search("[a-z]", password) and re.search("[A-Z]", password) and re.search("[0-9]", password) and re.search("[$#@]", password):
        print("Password is valid. Welcome!")
        break
    else:
        max_attempts -= 1
        if max_attempts > 0:
            print(f"Invalid password. You have", max_attempts, "attempts remaining.")
        else:
            print("Sorry, you've exceeded the maximum number of attempts. Access denied.")
