def is_palindrome(s):
    s = s.lower()
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

string_to_check = input("Enter the String to Check Palindrome or not: ")
result = is_palindrome(string_to_check)
if result:
    print(f"{string_to_check} is a palindrome.")
else:
    print(f"{string_to_check} is not a palindrome.")
