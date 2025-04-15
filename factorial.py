def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Test
print(factorial(5))  # Output: 120
print(factorial(10))  # Output: 3628800