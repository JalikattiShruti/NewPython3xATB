# Palindrome

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

input_str = input("Enter a string to check if it's a palindrome: ")

if is_palindrome(input_str):
    print(f'"{input_str}" is a palindrome.')
else:
    print(f'"{input_str}" is not a palindrome.')


