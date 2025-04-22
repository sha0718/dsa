def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print(is_palindrome("Race car"))  # True
print(is_palindrome("Hello, world"))  # False